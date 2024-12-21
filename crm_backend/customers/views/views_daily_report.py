from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Count, Q
from ..models import Customer
from sales.models import SalesUser


@login_required
def daily_report(request):
    # 获取时间范围，默认1天内
    today_date = datetime.today().strftime('%Y-%m-%d')
    start_date = request.GET.get('start_date', today_date)
    end_date = request.GET.get('end_date', today_date)

    # 获取选定的组长 ID（如果未选择则为 None）
    selected_leader_id = request.GET.get('group_leader')

    # 获取所有组长
    group_leaders = SalesUser.objects.filter(role='group_leader')

    # 如果选择了组长，筛选对应组员；否则默认筛选全公司
    if selected_leader_id:
        selected_leader = group_leaders.filter(id=selected_leader_id).first()
        group_members = SalesUser.objects.filter(group_leader=selected_leader)
    else:
        selected_leader = None
        group_members = SalesUser.objects.filter(group_leader__isnull=False)  # 仅筛选有组长的组员

    # 统计数据
    report_data = []
    overall_totals = {
        'total_customers': 0,
        'contacted_count': 0,
        'interested_count': 0,
        'joined_count': 0,
        'grade_a_count': 0,
        'considered_count': 0,
        'discussed_count': 0,
        'closed_count': 0,
    }

    for member in group_members:
        customers = Customer.objects.filter(
            created_by=member,
            created_at__date__range=[start_date, end_date]
        )

        # 统计数据
        total_customers = customers.count()
        contacted_count = customers.filter(is_contacted=True).count()
        interested_count = customers.filter(is_invited=True).count()
        joined_count = customers.filter(is_joined=True).count()
        grade_a_count = customers.filter(customer_level='A').count()
        considered_count = customers.filter(reconsider_checked=True).count()
        discussed_count = customers.filter(discuss_checked=True).count()
        closed_count = customers.filter(is_closed=True).count()

        # 计算率
        def calculate_rate(part, total):
            return round((part / total * 100) if total > 0 else 0.0, 2)

        report_data.append({
            'username': member.username,
            'total_customers': total_customers,
            'contacted_rate': calculate_rate(contacted_count, total_customers),
            'interested_rate': calculate_rate(interested_count, total_customers),
            'joined_rate': calculate_rate(joined_count, total_customers),
            'grade_a_rate': calculate_rate(grade_a_count, total_customers),
            'considered_rate': calculate_rate(considered_count, total_customers),
            'discussed_rate': calculate_rate(discussed_count, total_customers),
            'closed_rate': calculate_rate(closed_count, total_customers),  # 成交率
        })

        # 累计整体数据
        overall_totals['total_customers'] += total_customers
        overall_totals['contacted_count'] += contacted_count
        overall_totals['interested_count'] += interested_count
        overall_totals['joined_count'] += joined_count
        overall_totals['grade_a_count'] += grade_a_count
        overall_totals['considered_count'] += considered_count
        overall_totals['discussed_count'] += discussed_count
        overall_totals['closed_count'] += closed_count

    # 计算整体平均百分比
    def calculate_rate(part, total):
        return round((part / total * 100) if total > 0 else 0.0, 2)

    overall_rates = {
        'contacted_rate': calculate_rate(overall_totals['contacted_count'], overall_totals['total_customers']),
        'interested_rate': calculate_rate(overall_totals['interested_count'], overall_totals['total_customers']),
        'joined_rate': calculate_rate(overall_totals['joined_count'], overall_totals['total_customers']),
        'grade_a_rate': calculate_rate(overall_totals['grade_a_count'], overall_totals['total_customers']),
        'considered_rate': calculate_rate(overall_totals['considered_count'], overall_totals['total_customers']),
        'discussed_rate': calculate_rate(overall_totals['discussed_count'], overall_totals['total_customers']),
        'closed_rate': calculate_rate(overall_totals['closed_count'], overall_totals['total_customers']),
    }

    # 按成交率从高到低排序
    report_data.sort(key=lambda x: x['closed_rate'], reverse=True)

    return render(request, 'daily_report.html', {
        'report_data': report_data,
        'overall_rates': overall_rates,
        'group_leaders': group_leaders,
        'selected_leader': selected_leader,
        'start_date': start_date,
        'end_date': end_date,
        'overall_total_customers': overall_totals['total_customers'],  # 总客户数加总
    })