# customers/urls.py

from django.urls import path
from .views import customerlist, add_customer, customer_detail, edit_customer,delete_customer

urlpatterns = [
    path('customerlist/', customerlist, name='customerlist'),  # 定义 customerlist 路径
    path('add_customer/', add_customer, name='add_customer'),  # 添加 add_customer 路径
    path('customer/<int:id>/', customer_detail, name='customer_detail'),  # 详情页面
    path('edit-customer/<int:id>/', edit_customer, name='edit_customer'),  # 编辑页面
    path('delete_customer/<int:id>/', delete_customer, name='delete_customer'),
]