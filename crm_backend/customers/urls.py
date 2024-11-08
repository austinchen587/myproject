# customers/urls.py

from django.urls import path
from .views import (

    customerlist,
    add_customer,
    customer_detail,
    edit_customer,
    delete_customer,
    dashboard,
    data_analysis,
    analysis_data_json,
)

urlpatterns = [

    path('customerlist/', customerlist, name='customerlist'),  # 客户列表
    path('add_customer/', add_customer, name='add_customer'),
    path('customer/<int:id>/', customer_detail, name='customer_detail'),
    path('edit-customer/<int:id>/', edit_customer, name='edit_customer'),
    path('delete_customer/<int:id>/', delete_customer, name='delete_customer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('data_analysis/', data_analysis, name='data_analysis'),
    path('data_analysis_json/', analysis_data_json, name='data_analysis_json'),  # 添加此行
   

]