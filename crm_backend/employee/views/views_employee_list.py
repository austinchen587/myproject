from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Employee

def employee_list(request):
    status_filter = request.GET.get('status', '')  # 获取状态筛选条件
    employees = Employee.objects.all()

    if status_filter:
        employees = employees.filter(status=status_filter)

    paginator = Paginator(employees, 20)  # 每页 20 条数据
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/employee_list.html', {'employees': page_obj})