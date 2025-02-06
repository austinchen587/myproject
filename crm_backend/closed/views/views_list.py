from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import ClientData


def client_data_list(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")
    name = request.GET.get("name", "")
    phone = request.GET.get("phone", "")
    sales_teacher = request.GET.get("sales_teacher", "")
    deal_status = request.GET.get("deal_status", "")
    responsible_person = request.GET.get("responsible_person", "")

    # 初始查询集，按报名日期从近到远排序
    clients = ClientData.objects.order_by("-registration_date")

    # 日期范围筛选
    if start_date:
        clients = clients.filter(registration_date__gte=start_date)
    if end_date:
        clients = clients.filter(registration_date__lte=end_date)

    # 其他字段筛选
    if name:
        clients = clients.filter(name__icontains=name)
    if phone:
        clients = clients.filter(phone__icontains=phone)
    if sales_teacher:
        clients = clients.filter(sales_teacher__icontains=sales_teacher)
    if deal_status:
        clients = clients.filter(deal_status__icontains=deal_status)
    if responsible_person:
        clients = clients.filter(responsible_person__icontains=responsible_person)

    # 分页
    paginator = Paginator(clients, 20)  # 每页显示 20 条
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # 保留筛选条件的查询参数
    query_params = request.GET.copy()
    query_params.pop("page", None)  # 移除 page 参数
    query_string = query_params.urlencode()  # 编码查询参数

    # 渲染模板
    return render(request, "closed/closed_list.html", {
        "clients": page_obj,
        "query_string": query_string,  # 传递 URL 查询参数
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "phone": phone,
        "sales_teacher": sales_teacher,
        "deal_status": deal_status,
        "responsible_person": responsible_person
    })