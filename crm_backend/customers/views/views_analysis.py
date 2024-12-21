from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from customers.models import Customer
from django.http import JsonResponse
from sales.models import SalesUser
from datetime import datetime


@login_required
def data_analysis(request):
    customers = Customer.objects.all()

    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')

    totals = {
        key: sum(d[key] for d in analysis_data)
        for key in ['contacted_count', 'invited_count', 'wechat_added_count', 'joined_count', 'closed_count', 'total_count']
    }

    return render(request, 'data_analysis.html', {
        'analysis_data': analysis_data,
        'totals': totals,
    })


def analysis_data_json(request):
    user = request.user
    selected_user = request.GET.get('selected_user')
    selected_group = request.GET.get('selected_group')
    batch_number = request.GET.get('batch_number')

    # 获取客户数据
    customers = _get_filtered_customers(user, selected_user, selected_group, batch_number)

    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')

    return JsonResponse(list(analysis_data), safe=False)


@login_required
def product_manager_daily_report(request):
    today_date = datetime.today().strftime('%Y-%m-%d')
    start_date = request.GET.get('start_date', today_date)
    end_date = request.GET.get('end_date', today_date)

    leader_name = '汪城波'
    group_leader = SalesUser.objects.filter(username=leader_name).first()

    if not group_leader:
        return render(request, 'product_manager_daily_report.html', {'error': '指定的组长不存在'})

    group_members = SalesUser.objects.filter(group_leader=group_leader)
    user_id_to_username = {member.id: member.username for member in group_members}

    customers = Customer.objects.filter(
        product_manager_contact__in=user_id_to_username.values(),
        created_at__date__range=[start_date, end_date]
    )

    report_data = _generate_report(customers)

    total_summary = {
        key: sum(item[key] for item in report_data)
        for key in ['high_count', 'medium_count', 'low_count', 'total_count']
    }

    return render(request, 'product_manager_daily_report.html', {
        'start_date': start_date,
        'end_date': end_date,
        'group_leader': leader_name,
        'report_data': report_data,
        'total_summary': total_summary,
    })


def get_completion_data(request):
    user = request.user
    user_id = request.GET.get('user_id')
    group_id = request.GET.get('group_id')
    batch_number = request.GET.get('batch_number')

    customers = _get_filtered_customers(user, user_id, group_id, batch_number)

    total_customers = customers.count()
    fields = _get_completion_fields()

    field_completion = {label: 0 for _, label, _ in fields}

    for customer in customers:
        for field, label, default_value in fields:
            if getattr(customer, field) != default_value:
                field_completion[label] += 1

    completion_rates = {
        label: (count / total_customers * 100 if total_customers else 0)
        for label, count in field_completion.items()
    }

    return JsonResponse({'completion_rates': completion_rates})


# Helper Functions
def _get_filtered_customers(user, user_id, group_id, batch_number):
    """
    Helper function to filter customers based on user role and query params.
    """
    user_role = getattr(user, 'role', None)
    if user_role == 'admin':
        customers = Customer.objects.all()
    elif user_role == 'group_leader':
        customers = Customer.objects.filter(created_by__group_leader=user)
    else:
        customers = Customer.objects.filter(created_by=user)

    if user_id:
        customers = customers.filter(created_by_id=user_id)
    elif group_id:
        customers = customers.filter(created_by__group_leader_id=group_id)
    if batch_number:
        customers = customers.filter(student_batch=batch_number)

    return customers


def _get_completion_fields():
    """
    Returns the fields for calculating completion rates.
    """
    return [
        ('phone', '电话', ''),
        ('student_batch', '期数学员', 0),
        ('is_invited', '是否邀约', False),
        ('is_wechat_added', '是否加微信', False),
        ('is_joined', '是否入群', False),
        ('name', '姓名', '未知'),
        ('education', '学历', '大专'),
        ('city', '所在城市', 'Default City'),
        ('intention', '意向程度', '低'),
        ('is_closed', '是否成交', False),
        ('is_contacted', '是否接通', False),
    ]


def _generate_report(customers):
    """
    Helper function to generate product manager report data.
    """
    product_manager_contacts = customers.values_list('product_manager_contact', flat=True).distinct()
    report_data = []

    for product_manager in product_manager_contacts:
        customer_data = customers.filter(product_manager_contact=product_manager).values('intention').annotate(count=Count('intention'))
        intention_counts = {'高': 0, '中': 0, '低': 0}
        for data in customer_data:
            intention_counts[data['intention']] = data['count']

        total_count = sum(intention_counts.values())
        report_data.append({
            'product_manager': product_manager,
            'high_count': intention_counts['高'],
            'medium_count': intention_counts['中'],
            'low_count': intention_counts['低'],
            'total_count': total_count,
        })

    return report_data