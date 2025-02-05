from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Employee  # 确保正确导入模型
from django.utils.timezone import now, timedelta

def employee_list(request):

    # 获取当前日期 + 30 天
    today_plus_30 = (now().date() + timedelta(days=30)).strftime("%Y-%m-%d")

    # 获取筛选参数
    status = request.GET.get("status", "在职")  # 默认状态为 "在职"
    department = request.GET.get("department", "").strip()

    # 初始查询集
    employees = Employee.objects.all().order_by('-entry_date')

    # 状态筛选
    if status:
        employees = employees.filter(status=status)

    # 部门筛选
    if department:
        employees = employees.filter(department__icontains=department)

    # 分页逻辑
    paginator = Paginator(employees, 20)  # 每页显示 20 条
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employee/employee_list.html", {
        "employees": page_obj,
        "status": status,
        "department": department,
        "today_plus_30": today_plus_30,  # 传递当前日期 + 30 天
    })