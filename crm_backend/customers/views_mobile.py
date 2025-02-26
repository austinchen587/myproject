from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from .models import Customer, Recording,Comment,DescriptionHistory
import mimetypes
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
import json
from sales.models import SalesUser
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from django.db.models import Prefetch

@login_required
def mobile_view(request):
    today = datetime.today().date()
    default_start_date = today - timedelta(days=2)  # 默认显示最近2天

    # 获取筛选条件并提供默认值
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    phone_filter = request.GET.get('phone', '').strip()
    data_source_filter = request.GET.get('data_source', '').strip()
    student_batch_filter = request.GET.get('student_batch', '').strip()
    is_joined_filter = request.GET.get('is_joined', '').strip()
    created_by_filter = request.GET.get('created_by', '').strip()
    customer_level_filter = request.GET.get('customer_level', '').strip()  # 新增客户等级筛选条件

    # 日期处理
    try:
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        else:
            start_date = default_start_date  # 使用默认值

        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            end_date = today  # 使用默认值
    except ValueError:
        return JsonResponse({"error": "日期格式错误，请检查输入"}, status=400)

    # 转换为时区感知的 datetime
    start_datetime = make_aware(datetime.combine(start_date, datetime.min.time()))
    end_datetime = make_aware(datetime.combine(end_date, datetime.max.time()))

    # 初步筛选客户
    customers = Customer.objects.filter(created_at__range=(start_datetime, end_datetime))

    # 权限控制：普通用户只能查看自己的客户，组长可以查看本组客户，管理员查看所有客户
    if request.user.role == 'user':
        customers = customers.filter(created_by=request.user)
    elif request.user.role == 'group_leader':
        customers = customers.filter(created_by__group_leader=request.user)

    # 应用其他筛选条件
    if phone_filter:
        customers = customers.filter(phone__icontains=phone_filter)
    if data_source_filter:
        customers = customers.filter(data_source=data_source_filter)
    if student_batch_filter:
        if student_batch_filter.isdigit():
            customers = customers.filter(student_batch=int(student_batch_filter))
    if is_joined_filter in ['yes', 'no']:
        customers = customers.filter(is_joined=(is_joined_filter == 'yes'))
    if created_by_filter:
        if created_by_filter.isdigit():
            customers = customers.filter(created_by__id=int(created_by_filter))
    if customer_level_filter:
        customers = customers.filter(customer_level=customer_level_filter)  # 客户等级筛选

    # 按创建时间降序排列
    customers = customers.order_by('-created_at')


    # 使用 Prefetch 预加载描述历史记录
    customers = customers.prefetch_related(
        Prefetch(
            'description_history',
            queryset=DescriptionHistory.objects.order_by('-modified_at'),
            to_attr='description_history_list'
        )
    )

    # 获取所有 SalesUser 信息供筛选使用
    all_users = SalesUser.objects.filter(status='active')

    # 渲染模板，传递筛选上下文
    return render(request, 'mobile/mobile_sub/customer_list.html', {
        "customers": customers,
        "user": request.user,
        "all_users": all_users,
        "start_date": start_date,
        "end_date": end_date,
        "phone_filter": phone_filter,
        "data_source_filter": data_source_filter,
        "student_batch_filter": student_batch_filter,
        "is_joined_filter": is_joined_filter,
        "created_by_filter": created_by_filter,
        "customer_level_filter": customer_level_filter,  # 传递客户等级筛选值
    })


@login_required
def customer_detail_mobile(request, id):
    # 获取客户信息
    customer = get_object_or_404(Customer, id=id)

    # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限查看此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能查看本组的客户')
        return redirect('customerlist')

    # 获取描述历史，按修改时间降序排列
    description_history = customer.description_history.order_by('-modified_at')

    # 调试打印
    print(f"描述历史记录数量: {description_history.count()}")
    for history in description_history:
        print(f"- 新描述: {history.new_description}, 修改人: {history.modified_by}, 修改时间: {history.modified_at}")

    # 获取评论记录
    comments = customer.comments.all()

    # 如果是 POST 请求，处理添加评论逻辑
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                customer=customer,
                content=content,
                created_by=request.user,
            )
            messages.success(request, "评论添加成功")
            return redirect('customer_detail_mobile', id=customer.id)
        else:
            messages.error(request, "评论内容不能为空")

    # 渲染模板
    return render(request, 'mobile/mobile_sub/customer_detail.html', {
        'customer': customer,
        'description_history': description_history,
        'comments': comments,
    })

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def add_comment_ajax(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            content = body.get("content")
            customer_id = body.get("customer_id")

            if not content or not customer_id:
                return JsonResponse({"success": False, "error": "缺少必要参数"}, status=400)

            try:
                customer = Customer.objects.get(id=customer_id)
                comment = Comment.objects.create(
                    customer=customer,
                    content=content,
                    created_by=request.user,
                )
                return JsonResponse({
                    "success": True,
                    "comment": {
                        "content": comment.content,
                        "created_by": request.user.username,
                        "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    },
                })
            except Customer.DoesNotExist:
                return JsonResponse({"success": False, "error": "客户不存在"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "无效的JSON数据"}, status=400)
    return JsonResponse({"success": False, "error": "无效请求方法"}, status=405)





from django.utils.timezone import now, make_aware
from calendar import monthrange

@login_required
def closed_customer_detail(request):
    # 获取当前时间
    current_date = now().date()
    first_day_of_month = current_date.replace(day=1)  # 本月第一天
    last_day_of_month = current_date.replace(day=monthrange(current_date.year, current_date.month)[1])  # 本月最后一天

    # 获取筛选条件
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    phone_filter = request.GET.get('phone', '').strip()
    data_source_filter = request.GET.get('data_source', '').strip()
    student_batch_filter = request.GET.get('student_batch', '').strip()
    created_by_filter = request.GET.get('created_by', '').strip()
    customer_level_filter = request.GET.get('customer_level', '').strip()  # 新增客户等级筛选

    # 如果没有传入筛选条件，默认使用本月的第一天和最后一天
    try:
        if start_date:
            start_date = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
        else:
            start_date = make_aware(datetime.combine(first_day_of_month, datetime.min.time()))  # 本月第一天
    except ValueError:
        start_date = make_aware(datetime.combine(first_day_of_month, datetime.min.time()))

    try:
        if end_date:
            end_date = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
        else:
            end_date = make_aware(datetime.combine(last_day_of_month, datetime.max.time()))  # 本月最后一天
    except ValueError:
        end_date = make_aware(datetime.combine(last_day_of_month, datetime.max.time()))

    # 查询所有成交客户
    customers = Customer.objects.filter(is_closed=True, created_at__range=(start_date, end_date))

    # 手机号筛选
    if phone_filter and phone_filter.lower() != 'none':
        customers = customers.filter(phone__icontains=phone_filter)

    # 数据来源筛选
    if data_source_filter:
        customers = customers.filter(data_source=data_source_filter)

    # 学员期数筛选
    if student_batch_filter and student_batch_filter.isdigit():  # 检查是否为数字
        customers = customers.filter(student_batch=int(student_batch_filter))

    # 归属人筛选
    if created_by_filter and created_by_filter.isdigit():  # 检查是否为数字
        customers = customers.filter(created_by_id=int(created_by_filter))

    # 客户等级筛选
    if customer_level_filter:
        customers = customers.filter(customer_level=customer_level_filter)

    # 获取所有用户供筛选用
    all_users = SalesUser.objects.all()

    return render(request, 'mobile/mobile_sub/closed_customer.html', {
        'customers': customers,
        'start_date': start_date.date(),  # 返回给模板显示为日期
        'end_date': end_date.date(),      # 返回给模板显示为日期
        'phone_filter': phone_filter,
        'data_source_filter': data_source_filter,
        'student_batch_filter': student_batch_filter,
        'created_by_filter': created_by_filter,
        'customer_level_filter': customer_level_filter,  # 传递客户等级筛选
        'all_users': all_users,
    })