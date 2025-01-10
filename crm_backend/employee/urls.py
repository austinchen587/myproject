from django.urls import path
from .views import employee_list, add_employee, update_employee, delete_employee

app_name = 'employee'  # 为应用指定 app_name

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/add', add_employee, name='add_employee'),
    path('employees/edit/<int:id>', update_employee, name='update_employee'),
    path('employees/delete/<int:id>', delete_employee, name='delete_employee'),
]