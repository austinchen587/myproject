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
    get_completion_data,
    daily_report,
    product_manager_daily_report,
    
)

from .views_mobile import mobile_view, upload_audio ,customer_detail_mobile,add_comment_ajax # 导入新的视图函数

urlpatterns = [

    path('mobile/', mobile_view, name='mobile_view'),  # 定义手机端模板的路由
    path('mobile/customer/<int:id>/', customer_detail_mobile, name='customer_detail_mobile'),
    path('customerlist/', customerlist, name='customerlist'),  # 客户列表
    path('add_customer/', add_customer, name='add_customer'),
    path('customer/<int:id>/', customer_detail, name='customer_detail'),
    path('edit-customer/<int:id>/', edit_customer, name='edit_customer'),
    path('delete_customer/<int:id>/', delete_customer, name='delete_customer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('data_analysis/', data_analysis, name='data_analysis'),
    path('data_analysis_json/', analysis_data_json, name='data_analysis_json'),  # 添加此行
    path('get_completion_data/', get_completion_data, name='get_completion_data'),
    path('daily_report/', daily_report, name='daily_report'),
    path('<int:customer_id>/upload-audio/', upload_audio, name='upload_audio'),
    path('product_manager_daily_report/', product_manager_daily_report, name='product_manager_daily_report'),
    path('add_comment_ajax/', add_comment_ajax, name='add_comment_ajax'),
    
 

]