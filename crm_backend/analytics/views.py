from datetime import datetime, timedelta
from rest_framework import viewsets
from rest_framework.response import Response
from customers.models import Customer, SalesUser
from django.db.models import Count, Case, When, F, FloatField, ExpressionWrapper

class CustomerAnalysisViewSet(viewsets.ViewSet):
    def list(self, request):
        # 获取当前用户和请求参数
        user = request.user
        report_type = request.query_params.get('report_type', 'daily')
        group_id = request.query_params.get('group_id', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None) or datetime.today()

        # 处理自定义日期范围
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            # 根据报表类型设置默认时间范围
            if report_type == 'daily':
                start_date = end_date - timedelta(days=1)
            elif report_type == 'weekly': 
                start_date = end_date - timedelta(weeks=1)
            elif report_type == 'monthly':
                start_date = end_date - timedelta(days=30)

        # 根据用户权限筛选数据
        if user.role == 'user':
            customers = Customer.objects.filter(created_by=user)
        elif user.role == 'group_leader':
            customers = Customer.objects.filter(created_by__group_leader=user)
        elif user.role == 'admin':
            if group_id:
                group_leader = SalesUser.objects.get(id=group_id)
                group_members = SalesUser.objects.filter(group_leader_id=group_id) | SalesUser.objects.filter(id=group_leader.id)
                customers = Customer.objects.filter(created_by__in=group_members)
            else:
                customers = Customer.objects.all()

        # 日期过滤
        customers = customers.filter(created_at__range=[start_date, end_date])

        # 返回组长信息
        group_leaders = SalesUser.objects.filter(role='group_leader').values('id', 'username')

        # 全组总客户数
        total_group_customers = customers.count()

        # 客户数据统计
        customers_data = customers.values('created_by__username').annotate(
            total_customers=Count('id'),
            closed_customers=Count(Case(When(is_closed=True, then=1))),
            invited_customers=Count(Case(When(is_invited=True, then=1))),
            attended_first_live_customers=Count(Case(When(attended_first_live=True, then=1))),
            attended_second_live_customers=Count(Case(When(attended_second_live=True, then=1))),
            joined_customers=Count(Case(When(is_joined=True, then=1))),
            intention_mid=Count(Case(When(intention='中', then=1))),
            intention_high=Count(Case(When(intention='高', then=1))),
            contacted_customers=Count(Case(When(is_contacted=True, then=1))),  # 接通率
            wechat_added_customers=Count(Case(When(is_wechat_added=True, then=1))),  # 加微信率
            closed_ratio=ExpressionWrapper(F('closed_customers') * 100.0 / F('total_customers'), output_field=FloatField()),
            invited_ratio=ExpressionWrapper(F('invited_customers') * 100.0 / F('total_customers'), output_field=FloatField()),
            attended_first_live_ratio=ExpressionWrapper(F('attended_first_live_customers') * 100.0 / F('total_customers'), output_field=FloatField()),
            attended_second_live_ratio=ExpressionWrapper(F('attended_second_live_customers') * 100.0 / F('total_customers'), output_field=FloatField()),
            joined_ratio=ExpressionWrapper(F('joined_customers') * 100.0 / F('total_customers'), output_field=FloatField()),
            contacted_ratio=ExpressionWrapper(F('contacted_customers') * 100.0 / F('total_customers'), output_field=FloatField()),  # 接通率
            wechat_added_ratio=ExpressionWrapper(F('wechat_added_customers') * 100.0 / F('total_customers'), output_field=FloatField()),  # 加微信率
            intention_mid_ratio=ExpressionWrapper(F('intention_mid') * 100.0 / F('total_customers'), output_field=FloatField()),
            intention_high_ratio=ExpressionWrapper(F('intention_high') * 100.0 / F('total_customers'), output_field=FloatField())
        )

        # 汇总统计
        summary = {
            'total_customers': customers.count(),
            'total_closed': customers.filter(is_closed=True).count(),
            'total_invited': customers.filter(is_invited=True).count(),
            'attended_first_live': customers.filter(attended_first_live=True).count(),
            'attended_second_live': customers.filter(attended_second_live=True).count(),
            'joined_customers': customers.filter(is_joined=True).count(),
            'intention_mid': customers.filter(intention='中').count(),
            'intention_high': customers.filter(intention='高').count(),
            'contacted_customers': customers.filter(is_contacted=True).count(),  # 接通总数
            'wechat_added_customers': customers.filter(is_wechat_added=True).count(),  # 加微信总数
        }

        # 计算平均值 (averages)
        averages = {
            'intention_high_ratio': customers.filter(intention='高').count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'intention_mid_ratio': customers.filter(intention='中').count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'invited_ratio': customers.filter(is_invited=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'joined_ratio': customers.filter(is_joined=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'attended_first_live_ratio': customers.filter(attended_first_live=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'attended_second_live_ratio': customers.filter(attended_second_live=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'closed_ratio': customers.filter(is_closed=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,
            'contacted_ratio': customers.filter(is_contacted=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,  # 接通率
            'wechat_added_ratio': customers.filter(is_wechat_added=True).count() / total_group_customers * 100 if total_group_customers > 0 else 0,  # 加微信率
        }

        return Response({
            'data': customers_data,
            'summary': summary,
            'averages': averages,
            'total_group_customers': total_group_customers,
            'group_leaders': list(group_leaders)
        })