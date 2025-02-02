from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.http import QueryDict  # 用于处理查询参数
from ..models import ClientData

def client_data_list_follow(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")
    quick_filter = request.GET.get("quick_filter", "")
    responsible_person = request.GET.get("responsible_person", "")
    name = request.GET.get("name", "")
    is_on_leave = request.GET.get("is_on_leave", "")

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

    # 是否请假筛选（转换 "true"/"false" 为布尔值）
    if is_on_leave == "true":
        clients = clients.filter(is_on_leave=True)
    elif is_on_leave == "false":
        clients = clients.filter(is_on_leave=False)


    # 分页逻辑
    paginator = Paginator(clients, 20)  # 每页显示20条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 构造保留筛选条件的 URL 查询参数
    query_params = request.GET.copy()
    if "page" in query_params:
        del query_params["page"]  # 避免翻页时多次附加 page 参数

    query_string = query_params.urlencode()  # 将筛选参数转换为 URL 查询字符串

    # 将分页数据和筛选信息传递到模板
    return render(request, 'closed/closed_list_follow.html', {
        'clients': page_obj,
        'start_date': start_date,
        'end_date': end_date,
        'quick_filter': quick_filter,
        'responsible_person': responsible_person,  # 传递负责人筛选的值到模板
        'name': name,
        'query_string': query_string,  # 传递查询字符串到模板
        'is_on_leave': is_on_leave,
    })