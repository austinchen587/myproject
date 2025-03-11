from django.shortcuts import render
from django.db.models import Count
from datetime import datetime
from closed.models import Tag, ClientData  # 导入 ClientData 和 Tag 模型

def tag_statistics(request):
    # 获取时间范围参数
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    project = request.GET.get('project', None)
    responsible_person = request.GET.get('responsible_person', None)

    # 构建过滤条件
    filter_kwargs = {}
    if start_date:
        filter_kwargs['registration_date__gte'] = start_date  # 日期大于等于开始日期
    if end_date:
        filter_kwargs['registration_date__lte'] = end_date  # 日期小于等于结束日期
    if project:
        filter_kwargs['project'] = project  # 筛选项目
    if responsible_person:
        filter_kwargs['responsible_person__icontains'] = responsible_person  # 使用 responsible_person 进行筛选

    # 获取在时间范围内的客户数据
    clients_in_range = ClientData.objects.filter(**filter_kwargs)

    # 获取标签统计，每个标签的客户数量
    tag_counts = Tag.objects.filter(clients__in=clients_in_range).annotate(tag_count=Count('clients')).order_by('-tag_count')



    return render(request, 'closed/tag_statistics.html', {'tag_counts': tag_counts, 'tag_details': tag_details})