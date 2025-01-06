from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import ClientData

def client_data_list_follow(request):
    # 获取所有客户数据，按报名日期从近到远排序
    clients = ClientData.objects.order_by('-registration_date')
    
    # 分页逻辑
    paginator = Paginator(clients, 20)  # 每页显示20条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 将分页数据传递到模板
    return render(request, 'closed/closed_list_follow.html', {'clients': page_obj})