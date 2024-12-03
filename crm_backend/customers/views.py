from sales.models import SalesUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Customer, Recording
from .forms import CustomerForm
from django.http import JsonResponse
from .models import Customer  # 假设Customer模型定义了相关字段
from django.db.models import Count, Q, F
import mimetypes
import os
from django.utils.timezone import now

from .utils import calculate_completion_rate
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse


@login_required
def customerlist(request):
    # 获取当前时间和默认的过去2天时间范围
    now = timezone.now()
    two_days_ago = now - timezone.timedelta(days=2)

    # 如果没有筛选条件，则默认设置时间范围为过去2天
    start_date = request.GET.get('start_date') or two_days_ago.strftime('%Y-%m-%d')
    end_date = request.GET.get('end_date') or now.strftime('%Y-%m-%d')

    # 获取筛选条件的参数
    phone_filter = request.GET.get('phone', '')
    data_source_filter = request.GET.get('data_source', '')
    student_batch_filter = request.GET.get('student_batch', '')
    is_contacted_filter = request.GET.get('is_contacted', '')
    is_joined_filter = request.GET.get('is_joined', '')
    is_closed_filter = request.GET.get('is_closed', '')
    created_by_filter = request.GET.get('created_by', '')
    wechat_name_filter = request.GET.get('wechat_name', '')  # 新增的微信名筛选参数
    intention_filter = request.GET.get('intention', '')  # 客户意向程度筛选参数
    product_manager_contact_filter = request.GET.get('product_manager_contact', '')  # 产品经理对接人筛选参数

    # 初步时间筛选和排序
    customers = Customer.objects.filter(created_at__date__range=[start_date, end_date]).order_by('-created_at')

    # 权限控制：普通用户只能查看自己的客户，组长可以查看本组客户，管理员查看所有客户
    if request.user.role == 'user':
        customers = customers.filter(created_by=request.user)
    elif request.user.role == 'group_leader':
        customers = customers.filter(created_by__group_leader=request.user)

    # 应用筛选条件
    if phone_filter:
        customers = customers.filter(phone__icontains=phone_filter)
    if data_source_filter:
        customers = customers.filter(data_source=data_source_filter)
    if student_batch_filter:
        customers = customers.filter(student_batch=student_batch_filter)
    if is_contacted_filter:
        customers = customers.filter(is_contacted=(is_contacted_filter == 'yes'))
    if is_joined_filter:
        customers = customers.filter(is_joined=(is_joined_filter == 'yes'))
    if is_closed_filter:
        customers = customers.filter(is_closed=(is_closed_filter == 'yes'))
    if created_by_filter:
        customers = customers.filter(created_by__id=created_by_filter)
    if wechat_name_filter:  # 应用微信名筛选条件
        customers = customers.filter(wechat_name__icontains=wechat_name_filter)
    if intention_filter:  # 应用客户意向程度筛选条件
        customers = customers.filter(intention=intention_filter)
    if product_manager_contact_filter:  # 应用产品经理对接人筛选条件
        customers = customers.filter(product_manager_contact=product_manager_contact_filter)

    # 获取所有归属人用于筛选选择框
    all_users = SalesUser.objects.all()

    # 获取所有产品经理对接人选项
    product_manager_contacts = Customer.objects.values_list('product_manager_contact', flat=True).distinct()

    # 当前用户角色和组
    current_user_role = getattr(request.user, 'role', None)
    current_user_group_id = getattr(request.user, 'group_id', None)

    # 检查是否需要高亮显示
    for customer in customers:
        customer.needs_highlight = customer.created_by != customer.updated_by

    return render(request, 'customerlist.html', {
        'customers': customers,
        'start_date': start_date,
        'end_date': end_date,
        'phone_filter': phone_filter,
        'wechat_name_filter': wechat_name_filter,  # 传递微信名筛选参数
        'data_source_filter': data_source_filter,
        'student_batch_filter': student_batch_filter,
        'is_contacted_filter': is_contacted_filter,
        'is_joined_filter': is_joined_filter,
        'is_closed_filter': is_closed_filter,
        'created_by_filter': created_by_filter,
        'intention_filter': intention_filter,  # 传递客户意向筛选参数
        'product_manager_contact_filter': product_manager_contact_filter,  # 传递产品经理对接人筛选参数
        'all_users': all_users,
        'product_manager_contacts': product_manager_contacts,  # 传递产品经理对接人列表
        'current_user_role': current_user_role,
        'current_user_group_id': current_user_group_id,
    })





# 添加客户视图
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user  # 自动设置创建人
            customer.updated_by = request.user  # 自动设置为最后修改人
            customer.save()
            messages.success(request, '客户添加成功')
            return redirect('customerlist')
    else:
        form = CustomerForm()
    
    return render(request, 'add_customer.html', {'form': form})

@login_required
def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限编辑此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能编辑本组的客户')
        return redirect('customerlist')

    # 获取筛选条件
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    phone = request.GET.get('phone', '')
    data_source = request.GET.get('data_source', '')
    student_batch = request.GET.get('student_batch', '')
    is_contacted = request.GET.get('is_contacted', '')
    is_joined = request.GET.get('is_joined', '')
    is_closed = request.GET.get('is_closed', '')
    created_by = request.GET.get('created_by', '')

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_by = request.user  # 自动设置最后修改人
            customer.save()
            messages.success(request, '客户信息更新成功')
            # 保留筛选条件的重定向
            return redirect(f"{reverse('customerlist')}?start_date={start_date}&end_date={end_date}&phone={phone}&data_source={data_source}&student_batch={student_batch}&is_contacted={is_contacted}&is_joined={is_joined}&is_closed={is_closed}&created_by={created_by}")
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'edit_customer.html', {'form': form, 'customer': customer})

# 查看客户详情视图
@login_required
def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)

    # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限查看此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能查看本组的客户')
        return redirect('customerlist')

    return render(request, 'customer_detail.html', {'customer': customer})

# 删除客户视图
@login_required
def delete_customer(request, id):
    if request.method == "POST":
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        return JsonResponse({"success": True, "message": "客户删除成功"})
    return JsonResponse({"success": False, "message": "请求无效"})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def data_analysis(request):
    return render(request, 'data_analysis.html')


@login_required
def data_analysis(request):
    user = request.user
    user_role = getattr(user, 'role', None)
    
    # 获取所有用户（仅管理员）
    all_users = SalesUser.objects.all() if user_role == 'admin' else None
    
    # 获取所有组长（仅管理员）
    group_leaders = SalesUser.objects.filter(role='group_leader') if user_role == 'admin' else None
    
    # 获取组长的组员列表（仅组长）
    group_users = SalesUser.objects.filter(group_leader=user) if user_role == 'group_leader' else None
    
    # 根据角色获取客户数据
    if user_role == 'admin':
        customers = Customer.objects.all()
    elif user_role == 'group_leader':
        customers = Customer.objects.filter(created_by__group_leader=user)
    else:
        customers = Customer.objects.filter(created_by=user)

    # 检查获取到的客户数量
    print(f"客户数量: {customers.count()}")  # 仅用于调试，可以在控制台查看输出


    # 聚合数据按学员期数统计
    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')  # 降序排序

    # 计算汇总数据
    totals = {
        'contacted_count': sum([d['contacted_count'] for d in analysis_data]),
        'invited_count': sum([d['invited_count'] for d in analysis_data]),
        'wechat_added_count': sum([d['wechat_added_count'] for d in analysis_data]),
        'joined_count': sum([d['joined_count'] for d in analysis_data]),
        'closed_count': sum([d['closed_count'] for d in analysis_data]),
        'overall_total': sum([d['total_count'] for d in analysis_data]),
    }

    # 获取所有学员期数
    student_batches = Customer.objects.values_list('student_batch', flat=True).distinct().order_by('student_batch')

    return render(request, 'data_analysis.html', {
        'analysis_data': analysis_data,
        'totals': totals,
        'user_role': user_role,
        'all_users': all_users,
        'group_leaders': group_leaders,
        'group_users': group_users,
        'student_batches': student_batches,  # 传递学员期数列表
    })








def analysis_data_json(request):
    user = request.user
    user_role = getattr(user, 'role', None)
    selected_user = request.GET.get('selected_user')
    selected_group = request.GET.get('selected_group')
    batch_number = request.GET.get('batch_number')

    # 根据角色获取客户数据
    if user_role == 'admin':
        customers = Customer.objects.all()
    elif user_role == 'group_leader':
        customers = Customer.objects.filter(created_by__group_leader=user)
    else:
        customers = Customer.objects.filter(created_by=user)

    # 根据筛选条件进一步过滤客户数据
    if selected_user:
        customers = customers.filter(created_by_id=selected_user)
    elif selected_group:
        customers = customers.filter(created_by__group_leader_id=selected_group)
    if batch_number:
        customers = customers.filter(student_batch=batch_number)

    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')

    return JsonResponse(list(analysis_data), safe=False)





def get_completion_data(request):
    user = request.user
    user_role = getattr(user, 'role', None)
    user_id = request.GET.get('user_id')
    group_id = request.GET.get('group_id')
    batch_number = request.GET.get('batch_number')

    # 根据角色获取客户数据
    if user_role == 'admin':
        customers = Customer.objects.all()
    elif user_role == 'group_leader':
        customers = Customer.objects.filter(created_by__group_leader=user)
    else:
        customers = Customer.objects.filter(created_by=user)

    # 根据筛选条件进一步过滤客户数据
    if user_id:
        customers = customers.filter(created_by_id=user_id)
    elif group_id:
        customers = customers.filter(created_by__group_leader_id=group_id)
    if batch_number:
        customers = customers.filter(student_batch=batch_number)

    total_customers = customers.count()

    # 关键字段列表，包含默认值，用于计算完成度
    fields = [
        ('phone', '电话', ''),  # 假设空字符串是未填写状态
        ('student_batch', '期数学员', 0),  # 默认值0为未填写
        ('is_invited', '是否邀约', False), 
        ('is_wechat_added', '是否加微信', False), 
        ('is_joined', '是否入群', False),
        ('name', '姓名', '未知'),  # '未知'为默认值
        ('education', '学历', '大专'),  # '大专'为默认值
        ('city', '所在城市', 'Default City'),  # 'Default City'为默认值
        ('intention', '意向程度', '低'),  # '低'为默认值
        ('customer_needs_analysis', '需求分析', []),  # 空列表为未填写
        ('customer_personality_analysis', '性格分析', []), 
        ('cloud_computing_promotion_content', '推广内容', []),
        ('is_closed', '是否成交', False),
        ('is_contacted', '是否接通', False),
        ('data_source', '数据来源', 'AI数据'),  # 假设 'AI数据' 为默认
        ('wechat_name', '客户微信名', None),  # None 为未填写
        ('attended_first_live', '参加第一天直播', False),
        ('attended_second_live', '参加第二天直播', False),
        ('first_day_watch_duration', '第一天观看时长', 0),
        ('second_day_watch_duration', '第二天观看时长', 0),
        ('first_day_feedback', '第一天反馈', '一般'),
        ('second_day_feedback', '第二天反馈', '一般'),
        ('persona_chat', '人设聊天', False),
        ('additional_students', '马甲加学员', False),
        ('comments_count', '评论数', False),
        ('deal_7_days_checked', '7天成交', False),
        ('deal_14_days_checked', '14天成交', False),
        ('deal_21_days_checked', '21天成交', False)
    ]

    # 计算完成度
    field_completion = {label: 0 for _, label, _ in fields}

    for customer in customers:
        for field, label, default_value in fields:
            # 判断字段值是否不同于默认值
            if getattr(customer, field) != default_value:
                field_completion[label] += 1

    completion_rates = {
        label: (count / total_customers * 100 if total_customers else 0)
        for label, count in field_completion.items()
    }

    return JsonResponse({'completion_rates': completion_rates})





from datetime import datetime, timedelta

@login_required
def daily_report(request):
    # 获取当前用户角色和日期筛选条件
    user_role = request.user.role
    selected_leader_id = request.GET.get('group_leader', None)
    
    # 设置日期筛选，默认为当天
    today_date = datetime.today().strftime('%Y-%m-%d')
    selected_date = request.GET.get('date', today_date)

    # 获取所有组长供管理员选择
    group_leaders = SalesUser.objects.filter(role='group_leader') if user_role == 'admin' else []

    # 根据权限筛选用户
    if user_role == 'user':
        group_members = SalesUser.objects.filter(id=request.user.id)
    elif user_role == 'group_leader':
        group_members = SalesUser.objects.filter(Q(group_leader=request.user) | Q(id=request.user.id))
    elif user_role == 'admin' and selected_leader_id:
        selected_leader = SalesUser.objects.get(id=selected_leader_id)
        group_members = SalesUser.objects.filter(Q(group_leader=selected_leader) | Q(id=selected_leader.id))
    else:
        group_members = SalesUser.objects.none()

    # 构建透视表数据并计算汇总
    report_data = []
    total_summary = {
        'total_phone_count': 0,
        'is_contacted_count': 0,
        'is_invited_count': 0,
        'is_wechat_added_count': 0,
        'is_joined_count': 0,
        'product_manager_count': 0,  # 增加产品经理对接人统计
    }
    
    for member in group_members:
        # 根据筛选日期筛选客户数据
        total_phone_count = Customer.objects.filter(created_by=member, created_at__date=selected_date).count()
        is_contacted_count = Customer.objects.filter(created_by=member, is_contacted=True, created_at__date=selected_date).count()
        is_invited_count = Customer.objects.filter(created_by=member, is_invited=True, created_at__date=selected_date).count()
        is_wechat_added_count = Customer.objects.filter(created_by=member, is_wechat_added=True, created_at__date=selected_date).count()
        is_joined_count = Customer.objects.filter(created_by=member, is_joined=True, created_at__date=selected_date).count()
        
        # 统计产品经理对接人非默认值的数量
        product_manager_count = Customer.objects.filter(
            created_by=member,
            created_at__date=selected_date
        ).exclude(product_manager_contact='未分配').count()

        # 计算百分比，保留两位小数
        report_data.append({
            'username': member.username,
            'total_phone_count': total_phone_count,
            'is_contacted_count': is_contacted_count,
            'is_contacted_percent': round((is_contacted_count / total_phone_count) * 100, 2) if total_phone_count else 0,
            'is_invited_count': is_invited_count,
            'is_invited_percent': round((is_invited_count / total_phone_count) * 100, 2) if total_phone_count else 0,
            'is_wechat_added_count': is_wechat_added_count,
            'is_wechat_added_percent': round((is_wechat_added_count / total_phone_count) * 100, 2) if total_phone_count else 0,
            'is_joined_count': is_joined_count,
            'is_joined_percent': round((is_joined_count / total_phone_count) * 100, 2) if total_phone_count else 0,
            'product_manager_count': product_manager_count,
            'product_manager_percent': round((product_manager_count / total_phone_count) * 100, 2) if total_phone_count else 0,
        })

        # 更新汇总数据
        total_summary['total_phone_count'] += total_phone_count
        total_summary['is_contacted_count'] += is_contacted_count
        total_summary['is_invited_count'] += is_invited_count
        total_summary['is_wechat_added_count'] += is_wechat_added_count
        total_summary['is_joined_count'] += is_joined_count
        total_summary['product_manager_count'] += product_manager_count

    # 汇总百分比
    if total_summary['total_phone_count'] > 0:
        total_summary['is_contacted_percent'] = round((total_summary['is_contacted_count'] / total_summary['total_phone_count']) * 100, 2)
        total_summary['is_invited_percent'] = round((total_summary['is_invited_count'] / total_summary['total_phone_count']) * 100, 2)
        total_summary['is_wechat_added_percent'] = round((total_summary['is_wechat_added_count'] / total_summary['total_phone_count']) * 100, 2)
        total_summary['is_joined_percent'] = round((total_summary['is_joined_count'] / total_summary['total_phone_count']) * 100, 2)
        total_summary['product_manager_percent'] = round((total_summary['product_manager_count'] / total_summary['total_phone_count']) * 100, 2)
    else:
        total_summary['is_contacted_percent'] = 0
        total_summary['is_invited_percent'] = 0
        total_summary['is_wechat_added_percent'] = 0
        total_summary['is_joined_percent'] = 0
        total_summary['product_manager_percent'] = 0

    return render(request, 'daily_report.html', {
        'group_leaders': group_leaders,
        'selected_leader_id': selected_leader_id,
        'selected_date': selected_date,
        'today_date': today_date,
        'report_data': report_data,
        'total_summary': total_summary,
        'user_role': user_role,
    })



@login_required
def mobile_view(request):
    # 获取所有客户数据
    customers = Customer.objects.all()
    return render(request, 'mobile_customer.html', {"customers": customers})



from django.utils.timezone import make_aware

def mobile_view(request):
    today = datetime.today().date()
    default_start_date = today - timedelta(days=5)

    start_date = request.GET.get('start_date', default_start_date)
    end_date = request.GET.get('end_date', today)

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    # 使用 make_aware 将 naive datetime 转换为 aware datetime
    start_datetime = make_aware(datetime.combine(start_date, datetime.min.time()))
    end_datetime = make_aware(datetime.combine(end_date, datetime.max.time()))

    customers = Customer.objects.filter(created_at__range=(start_datetime, end_datetime))

    return render(request, 'mobile_customer.html', {
        "customers": customers,
        "user": request.user,
        "start_date": start_date,
        "end_date": end_date,
    })


import logging

logger = logging.getLogger(__name__)

# 手动注册缺失的 MIME 类型
mimetypes.add_type("audio/x-m4a", ".m4a")
mimetypes.add_type("audio/ogg", ".ogg")

def upload_audio(request, customer_id):
    """
    处理客户音频文件上传
    """
    if request.method == "POST":
        # 日志调试：输出请求中的文件信息
        print(f"Request FILES: {request.FILES}")

        # 检查是否接收到文件
        if "audio" not in request.FILES:
            print("音频文件字段缺失")
            return JsonResponse({"error": "未接收到音频文件"}, status=400)

        audio_file = request.FILES["audio"]
        print(f"文件名: {audio_file.name}, 文件大小: {audio_file.size}")

        # 检查文件扩展名
        file_extension = os.path.splitext(audio_file.name)[1].lower()
        allowed_extensions = [".wav", ".mp3", ".m4a", ".ogg", ".flac"]
        if file_extension not in allowed_extensions:
            print(f"不支持的文件扩展名: {file_extension}")
            return JsonResponse({"error": f"不支持的文件扩展名: {file_extension}"}, status=400)

        # 检查 MIME 类型
        mime_type, _ = mimetypes.guess_type(audio_file.name)
        allowed_types = ["audio/wav", "audio/mpeg", "audio/x-m4a", "audio/ogg", "audio/flac"]
        if not mime_type or mime_type not in allowed_types:
            print(f"MIME 类型未检测到或不支持: {mime_type}")
            if file_extension not in allowed_extensions:
                return JsonResponse({"error": f"不支持的文件类型: {mime_type}"}, status=400)
            print(f"MIME 类型为空，扩展名检查通过: {file_extension}")

        # 保存文件
        customer = get_object_or_404(Customer, id=customer_id)
        customer.audio_file.save(audio_file.name, audio_file, save=True)

        return JsonResponse({"message": "音频文件上传成功！", "file_url": customer.audio_file.url})

    print("收到无效的请求")
    return JsonResponse({"error": "无效的请求"}, status=400)



@login_required
def product_manager_daily_report(request):
    # 获取当前日期
    today_date = datetime.today().strftime('%Y-%m-%d')
    start_date = request.GET.get('start_date', today_date)  # 获取自定义开始日期
    end_date = request.GET.get('end_date', today_date)      # 获取自定义结束日期

    # 指定的组长
    leader_name = '汪城波'
    group_leader = SalesUser.objects.filter(username=leader_name).first()

    if not group_leader:
        return render(request, 'product_manager_daily_report.html', {
            'error': '指定的组长不存在',
        })

    # 获取组长下的所有组员
    group_members = SalesUser.objects.filter(group_leader=group_leader)

    # 构建成员映射：user_id -> username
    user_id_to_username = {member.id: member.username for member in group_members}

    # 筛选客户数据：产品经理对接人是汪城波组下成员用户名
    customers = Customer.objects.filter(
        product_manager_contact__in=user_id_to_username.values(),
        created_at__date__range=[start_date, end_date]
    )

    # 统计每个产品经理对接人的客户意向
    report_data = []
    product_manager_contacts = customers.values_list('product_manager_contact', flat=True).distinct()

    for product_manager in product_manager_contacts:
        # 统计该产品经理对接人的客户意向
        customer_data = customers.filter(product_manager_contact=product_manager).values('intention').annotate(count=Count('intention'))

        # 初始化意向统计
        intention_counts = {
            '高': 0,
            '中': 0,
            '低': 0
        }

        # 填充统计数据
        for data in customer_data:
            intention_counts[data['intention']] = data['count']

        # 汇总总计
        total_count = sum(intention_counts.values())

        # 添加统计结果
        report_data.append({
            'product_manager': product_manager,  # 产品经理对接人
            'high_count': intention_counts['高'],
            'medium_count': intention_counts['中'],
            'low_count': intention_counts['低'],
            'total_count': total_count,
        })

    # 汇总统计
    total_summary = {
        'high_count': sum(data['high_count'] for data in report_data),
        'medium_count': sum(data['medium_count'] for data in report_data),
        'low_count': sum(data['low_count'] for data in report_data),
        'total_count': sum(data['total_count'] for data in report_data),
    }

    return render(request, 'product_manager_daily_report.html', {
        'start_date': start_date,
        'end_date': end_date,
        'group_leader': leader_name,
        'report_data': report_data,
        'total_summary': total_summary,
    })