from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import ClientData

def client_data_list(request):
    clients = ClientData.objects.order_by('-registration_date')  # 按报名日期从近到远排序
    paginator = Paginator(clients, 20)  # 每页显示20条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'closed/closed_list.html', {'clients': page_obj})