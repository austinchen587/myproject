from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from ..models import ClientData

def client_data_list_follow(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    quick_filter = request.GET.get("quick_filter")
    responsible_person = request.GET.get("responsible_person")  # 新增负责人的筛选参数
    name = request.GET.get("name")

    # 初始查询集
    clients = ClientData.objects.order_by('-registration_date')

    # 日期范围筛选
    if start_date:
        clients = clients.filter(registration_date__gte=start_date)
    if end_date:
        clients = clients.filter(registration_date__lte=end_date)

    # 快捷筛选逻辑
    if quick_filter == "3_days":
        filter_date = now().date() - timedelta(days=3)
        clients = clients.filter(registration_date__gte=filter_date)
    elif quick_filter == "4_15_days":
        start_date = now().date() - timedelta(days=15)
        end_date = now().date() - timedelta(days=4)
        clients = clients.filter(registration_date__range=(start_date, end_date))
    elif quick_filter == "16_30_days":
        start_date = now().date() - timedelta(days=30)
        end_date = now().date() - timedelta(days=16)
        clients = clients.filter(registration_date__range=(start_date, end_date))
    elif quick_filter == "30_plus_days":
        filter_date = now().date() - timedelta(days=30)
        clients = clients.filter(registration_date__lt=filter_date)

    # 负责人筛选
    if responsible_person:
        clients = clients.filter(responsible_person__icontains=responsible_person)

    if name:
        clients = clients.filter(name__icontains=name)

    # 分页逻辑
    paginator = Paginator(clients, 20)  # 每页显示20条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 将分页数据和筛选信息传递到模板
    return render(request, 'closed/closed_list_follow.html', {
        'clients': page_obj,
        'start_date': start_date,
        'end_date': end_date,
        'quick_filter': quick_filter,
        'responsible_person': responsible_person,  # 传递负责人筛选的值到模板
        'name': name,
    })