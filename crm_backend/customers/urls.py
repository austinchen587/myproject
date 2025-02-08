from django.urls import path
from .views_mobile_images import test_customer_images_view
from .views_mobile import mobile_view, customer_detail_mobile, add_comment_ajax, closed_customer_detail
from .views_mobile_audio import upload_audio, delete_audio
from .views_mobile_images import upload_image, delete_image
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
    check_new_comments,
    get_customer_detail,
)

urlpatterns = [
    # 移动端相关路由
    path('mobile/', mobile_view, name='mobile_view'),
    path('mobile/customer/<int:id>/', customer_detail_mobile, name='customer_detail_mobile'),
    path('add_comment_ajax/', add_comment_ajax, name='add_comment_ajax'),
    path('closed_customer/', closed_customer_detail, name='closed_customer_detail'),

    # 音频相关路由
    path('customers/recording/upload/<int:customer_id>/', upload_audio, name='upload_audio'),
    path('customers/recording/delete/<int:recording_id>/', delete_audio, name='delete_audio'),

    # 图片相关路由
    path('upload_image/<int:customer_id>/', upload_image, name='upload_image'),
    path('delete-image/<int:recording_id>/', delete_image, name='delete_image'),
    #path('customer-images/<int:customer_id>/', customer_images_view, name='customer_images_view'),
    #path('test-customer-images/<int:customer_id>/', customer_images_view, name='test_customer_images_view'),
    path('test-customer-images/<int:customer_id>/', test_customer_images_view, name='test_customer_images_view'),

    
    

    # 客户详情路由
    path('customer-detail/<int:customer_id>/', customer_detail, name='customer_detail'),

    # 核心功能路由
    path('customerlist/', customerlist, name='customerlist'),
    path('check_new_comments/', check_new_comments, name='check_new_comments'),
    path('api/customer/<int:customer_id>/', get_customer_detail, name='get_customer_detail'),
    path('add_customer/', add_customer, name='add_customer'),
    path('customer/<int:id>/', customer_detail, name='customer_detail'),
    path('edit-customer/<int:id>/', edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('data_analysis/', data_analysis, name='data_analysis'),
    path('data_analysis_json/', analysis_data_json, name='data_analysis_json'),
    path('get_completion_data/', get_completion_data, name='get_completion_data'),
    path('daily_report/', daily_report, name='daily_report'),
    path('product_manager_daily_report/', product_manager_daily_report, name='product_manager_daily_report'),
]