from django.shortcuts import render, get_object_or_404
from .models import Customer
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def customer_list(request):
    # 获取筛选条件
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    phone_filter = request.GET.get('phone', '').strip()
    wechat_name_filter = request.GET.get('wechat_name', '').strip()
    data_source_filter = request.GET.get('data_source', '').strip()
    is_contacted_filter = request.GET.get('is_contacted', '').strip()
    is_closed_filter = request.GET.get('is_closed', '').strip()

    # 构建查询条件
    filters = {}
    if start_date:
        filters['created_at__gte'] = start_date
    if end_date:
        filters['created_at__lte'] = end_date
    if phone_filter:
        filters['phone__icontains'] = phone_filter
    if wechat_name_filter:
        filters['wechat_name__icontains'] = wechat_name_filter
    if data_source_filter:
        filters['data_source'] = data_source_filter
    if is_contacted_filter:
        filters['is_contacted'] = (is_contacted_filter == 'yes')
    if is_closed_filter:
        filters['is_closed'] = (is_closed_filter == 'yes')

    # 根据角色过滤客户
    if request.user.role == 'user':
        filters['created_by'] = request.user
    elif request.user.role == 'group_leader':
        filters['created_by__group_leader'] = request.user  # 假设组长字段为 group_leader


    # 查询客户
    customers = Customer.objects.filter(**filters).order_by('-created_at')  # 从近到远排序

    # 分页功能
    paginator = Paginator(customers, 10)  # 每页显示 10 条记录
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 上下文
    context = {
        'page_obj': page_obj,  # 分页对象
        'start_date': start_date,
        'end_date': end_date,
        'phone_filter': phone_filter,
        'wechat_name_filter': wechat_name_filter,
        'data_source_filter': data_source_filter,
        'is_contacted_filter': is_contacted_filter,
        'is_closed_filter': is_closed_filter,
        'all_data_sources': ['AI数据', '视频号', '国开数据', '其他'],  # 示例筛选项
    }

    return render(request, 'new_customer_list/customer_list.html', context)

@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
        # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限查看此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能查看本组的客户')
        return redirect('customerlist')
    return render(request, 'new_customer_list/customer_detail.html', {'customer': customer})

@login_required
def add_customer(request):
    # 添加客户的逻辑
    return render(request, 'new_customer_list/add_customer.html')

@login_required
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    
    # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限编辑此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能编辑本组的客户')
        return redirect('customerlist')

    # 编辑逻辑（假设使用表单处理）
    if request.method == 'POST':
        # 表单逻辑
        pass

    return render(request, 'new_customer_list/edit_customer.html', {'customer': customer})


