from sales.models import SalesUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Customer
from .forms import CustomerForm
from django.http import JsonResponse
from .models import Customer  # 假设Customer模型定义了相关字段
from django.db.models import Count, Q



@login_required
def customerlist(request):
    now = timezone.now()
    five_days_ago = now - timezone.timedelta(days=5)
    start_date = request.GET.get('start_date', five_days_ago.strftime('%Y-%m-%d'))
    end_date = request.GET.get('end_date', now.strftime('%Y-%m-%d'))

    # 获取筛选字段的参数
    phone_filter = request.GET.get('phone', '')
    data_source_filter = request.GET.get('data_source', '')
    student_batch_filter = request.GET.get('student_batch', '')
    is_contacted_filter = request.GET.get('is_contacted', '')
    is_joined_filter = request.GET.get('is_joined', '')
    is_closed_filter = request.GET.get('is_closed', '')
    created_by_filter = request.GET.get('created_by', '')

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

    # 获取所有归属人用于筛选选择框
    all_users = SalesUser.objects.all()

    current_user_role = getattr(request.user, 'role', None)
    current_user_group_id = getattr(request.user, 'group_id', None)

    return render(request, 'customerlist.html', {
        'customers': customers,
        'start_date': start_date,
        'end_date': end_date,
        'phone_filter': phone_filter,
        'data_source_filter': data_source_filter,
        'student_batch_filter': student_batch_filter,
        'is_contacted_filter': is_contacted_filter,
        'is_joined_filter': is_joined_filter,
        'is_closed_filter': is_closed_filter,
        'created_by_filter': created_by_filter,
        'all_users': all_users,
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

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_by = request.user  # 自动设置最后修改人
            customer.save()
            messages.success(request, '客户信息更新成功')
            return redirect('customerlist')
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

    return render(request, 'data_analysis.html', {
        'analysis_data': analysis_data,
        'totals': totals,
        'user_role': user_role,
        'all_users': all_users,
        'group_leaders': group_leaders,
        'group_users': group_users,  # 传递组员列表
    })








def analysis_data_json(request):
    selected_user = request.GET.get('selected_user')
    selected_group = request.GET.get('selected_group')
    customers = Customer.objects.all()

    if selected_user:
        customers = customers.filter(created_by_id=selected_user)
    elif selected_group:
        customers = customers.filter(created_by__group_leader_id=selected_group)

    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')  # 降序排列

    return JsonResponse(list(analysis_data), safe=False)