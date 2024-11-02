from sales.models import SalesUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Customer
from .forms import CustomerForm

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
    customer = get_object_or_404(Customer, id=id)

    # 权限检查
    if request.user.role == 'user':
        messages.error(request, '您没有权限删除此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能删除本组的客户')
        return redirect('customerlist')

    customer.delete()
    messages.success(request, '客户删除成功')
    return redirect('customerlist')