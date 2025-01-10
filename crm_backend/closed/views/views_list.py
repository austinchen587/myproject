from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import ClientData


def client_data_list(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    name = request.GET.get("name")
    phone = request.GET.get("phone")
    sales_teacher = request.GET.get("sales_teacher")
    deal_status = request.GET.get("deal_status")
    responsible_person = request.GET.get("responsible_person")

    # 初始查询集，按报名日期从近到远排序
    clients = ClientData.objects.order_by("-registration_date")

    # 日期范围筛选
    if start_date:
        clients = clients.filter(registration_date__gte=start_date)
    if end_date:
        clients = clients.filter(registration_date__lte=end_date)

    # 字段筛选
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

    # 打印查询集调试
    print(clients.query)

    # 分页
    paginator = Paginator(clients, 20)  # 每页显示20条
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # 打印分页对象调试
    print(page_obj.object_list)

    # 渲染模板
    return render(request, "closed/closed_list.html", {"clients": page_obj})