from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from customers.models import Customer
from sales.models import SalesUser
from datetime import datetime
from django.utils.timezone import now

@login_required
def data_analysis(request):
    """
    数据分析视图
    """
    # 获取筛选条件
    selected_user = request.GET.get('selected_user')  # 用户筛选
    selected_group = request.GET.get('selected_group')  # 组筛选
    batch_number = request.GET.get('batch_number')  # 学员期数筛选

    # 仅获取有组长的客户
    customers = Customer.objects.filter(created_by__group_leader__isnull=False)

    # 应用筛选条件
    if selected_user:
        customers = customers.filter(created_by_id=selected_user)
    if selected_group:
        customers = customers.filter(created_by__group_leader_id=selected_group)
    if batch_number:
        customers = customers.filter(student_batch=batch_number)

    # 统计数据
    analysis_data = customers.values('student_batch').annotate(
        contacted_count=Count('id', filter=Q(is_contacted=True)),
        invited_count=Count('id', filter=Q(is_invited=True)),
        wechat_added_count=Count('id', filter=Q(is_wechat_added=True)),
        joined_count=Count('id', filter=Q(is_joined=True)),
        grade_a_count=Count('id', filter=Q(customer_level='A')),
        considered_count=Count('id', filter=Q(reconsider_checked=True)),  # 考虑率字段
        discussed_count=Count('id', filter=Q(discuss_checked=True)),  # 商量率字段
        closed_count=Count('id', filter=Q(is_closed=True)),
        total_count=Count('id')
    ).order_by('-student_batch')

    # 在分析数据中计算比率并添加字段
    for item in analysis_data:
        total = item['total_count']
        item['contacted_rate'] = (item['contacted_count'] / total * 100) if total > 0 else 0
        item['invited_rate'] = (item['invited_count'] / total * 100) if total > 0 else 0
        item['wechat_added_rate'] = (item['wechat_added_count'] / total * 100) if total > 0 else 0
        item['joined_rate'] = (item['joined_count'] / total * 100) if total > 0 else 0
        item['grade_a_rate'] = (item['grade_a_count'] / total * 100) if total > 0 else 0
        item['considered_rate'] = (item['considered_count'] / total * 100) if total > 0 else 0
        item['discussed_rate'] = (item['discussed_count'] / total * 100) if total > 0 else 0
        item['closed_rate'] = (item['closed_count'] / total * 100) if total > 0 else 0

    # 汇总数据
    totals = {
        key: sum(d[key] for d in analysis_data)
        for key in ['contacted_count', 'invited_count', 'wechat_added_count', 'joined_count', 'grade_a_count', 'considered_count', 'discussed_count', 'closed_count', 'total_count']
    }
    totals.update({
        'contacted_rate': (totals['contacted_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'invited_rate': (totals['invited_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'wechat_added_rate': (totals['wechat_added_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'joined_rate': (totals['joined_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'grade_a_rate': (totals['grade_a_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'considered_rate': (totals['considered_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'discussed_rate': (totals['discussed_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
        'closed_rate': (totals['closed_count'] / totals['total_count'] * 100) if totals['total_count'] else 0,
    })

    # 获取所有用户和组长用于筛选
    all_users = SalesUser.objects.filter(group_leader__isnull=False).distinct()
    group_leaders = SalesUser.objects.filter(role='group_leader').distinct()
    student_batches = Customer.objects.values_list('student_batch', flat=True).distinct()

    return render(request, 'data_analysis/data_analysis.html', {
        'analysis_data': analysis_data,
        'totals': totals,
        'all_users': all_users,
        'group_leaders': group_leaders,
        'student_batches': student_batches,
        'selected_user': selected_user,
        'selected_group': selected_group,
        'batch_number': batch_number,
    })


@login_required
def analysis_data_json(request):
    """
    动态获取分析数据，用于前端表格展示
    """
    user = request.user
    selected_user = request.GET.get('selected_user')
    selected_group = request.GET.get('selected_group')
    batch_number = request.GET.get('batch_number')

    # 获取筛选后的客户数据
    customers = _get_filtered_customers(user, selected_user, selected_group, batch_number)

    # 统计数据
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
    """
    产品经理日报视图，按产品经理统计客户意向
    """
    today_date = now().strftime('%Y-%m-%d')
    start_date = request.GET.get('start_date', today_date)
    end_date = request.GET.get('end_date', today_date)

    leader_name = '汪城波'
    group_leader = SalesUser.objects.filter(username=leader_name).first()

    if not group_leader:
        return render(request, 'data_analysis/product_manager_daily_report.html', {'error': '指定的组长不存在'})

    # 筛选组员及其客户
    group_members = SalesUser.objects.filter(group_leader=group_leader)
    user_id_to_username = {member.id: member.username for member in group_members}
    customers = Customer.objects.filter(
        product_manager_contact__in=user_id_to_username.values(),
        created_at__date__range=[start_date, end_date]
    )

    # 生成日报数据
    report_data = _generate_report(customers)

    # 汇总数据
    total_summary = {
        key: sum(item[key] for item in report_data)
        for key in ['high_count', 'medium_count', 'low_count', 'total_count']
    }

    return render(request, 'data_analysis/product_manager_daily_report.html', {
        'start_date': start_date,
        'end_date': end_date,
        'group_leader': leader_name,
        'report_data': report_data,
        'total_summary': total_summary,
    })


@login_required
def get_completion_data(request):
    """
    动态获取客户完成度数据，用于前端雷达图展示
    """
    user = request.user
    user_id = request.GET.get('user_id')
    group_id = request.GET.get('group_id')
    batch_number = request.GET.get('batch_number')

    # 筛选客户数据
    customers = _get_filtered_customers(user, user_id, group_id, batch_number)

    # 初始化统计字段
    total_customers = customers.count()
    fields = _get_completion_fields()
    field_completion = {label: 0 for _, label, _ in fields}

    # 统计完成度
    for customer in customers:
        for field, label, default_value in fields:
            if getattr(customer, field) != default_value:
                field_completion[label] += 1

    # 计算完成率
    completion_rates = {
        label: (count / total_customers * 100 if total_customers else 0)
        for label, count in field_completion.items()
    }

    return JsonResponse({'completion_rates': completion_rates})


# Helper Functions
def _get_filtered_customers(user, user_id, group_id, batch_number):
    """
    筛选客户数据，支持用户角色和动态筛选条件
    """
    user_role = getattr(user, 'role', None)
    if user_role == 'admin':
        customers = Customer.objects.all()
    elif user_role == 'group_leader':
        customers = Customer.objects.filter(created_by__group_leader=user)
    else:
        customers = Customer.objects.filter(created_by=user)

    # 动态筛选条件
    if user_id:
        customers = customers.filter(created_by_id=user_id)
    elif group_id:
        customers = customers.filter(created_by__group_leader_id=group_id)
    if batch_number:
        customers = customers.filter(student_batch=batch_number)

    return customers


def _get_completion_fields():
    """
    获取需要统计完成度的字段及其默认值
    """
    return [
        ('phone', '电话', ''),
        ('student_batch', '期数学员', 0),
        ('is_invited', '是否邀约', False),
        ('is_wechat_added', '是否加微信', False),
        ('is_joined', '是否入群', False),
        ('name', '姓名', '未知'),
        ('education', '学历', '大专以下'),
        ('city', '所在城市', '未知'),
        ('intention', '意向程度', '低'),
        ('is_closed', '是否成交', False),
        ('is_contacted', '是否接通', False),
    ]


def _generate_report(customers):
    """
    生成产品经理的客户意向统计报告
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