from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sales.models import SalesUser
from ..models import Customer
from django.utils import timezone

@login_required
def customerlist(request):
    # 获取当前时间和默认时间范围
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
    wechat_name_filter = request.GET.get('wechat_name', '')
    customer_level_filter = request.GET.get('customer_level', '')  # 替换客户意向程度筛选

    product_manager_contact_filter = request.GET.get('product_manager_contact', '')

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
    if wechat_name_filter:
        customers = customers.filter(wechat_name__icontains=wechat_name_filter)
    if customer_level_filter:  # 新增客户等级筛选
        customers = customers.filter(customer_level=customer_level_filter)
    if product_manager_contact_filter:
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

    return render(request, 'x_customer_list/customer_list.html', {
        'customers': customers,
        'start_date': start_date,
        'end_date': end_date,
        'phone_filter': phone_filter,
        'wechat_name_filter': wechat_name_filter,
        'data_source_filter': data_source_filter,
        'student_batch_filter': student_batch_filter,
        'is_contacted_filter': is_contacted_filter,
        'is_joined_filter': is_joined_filter,
        'is_closed_filter': is_closed_filter,
        'created_by_filter': created_by_filter,
        'customer_level_filter': customer_level_filter,  # 新增筛选条件
        'product_manager_contact_filter': product_manager_contact_filter,
        'all_users': all_users,
        'product_manager_contacts': product_manager_contacts,
        'current_user_role': current_user_role,
        'current_user_group_id': current_user_group_id,
    })