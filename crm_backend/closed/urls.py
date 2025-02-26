from django.urls import path
from .views import client_data_list, add_client, update_client, delete_client, client_data_list_follow, update_client_follow, sales_analysis_view, assign_tags_to_client, tag_statistics

app_name = 'closed'  # 为应用指定 app_name

urlpatterns = [
    path('client-data-list/', client_data_list, name='client_data_list'),
    path('add-client/', add_client, name='add_client'),  # 定义添加客户的路由
    path('update-client/<int:client_id>/', update_client, name='update_client'),  # 更新客户信息
    path('delete-client/<int:client_id>/', delete_client, name='delete_client'),  # 删除客户信息
    path('client-data-list-follow/', client_data_list_follow, name='client_data_list_follow'),
    path('update-client-follow/<int:client_id>/', update_client_follow, name='update_client_follow'),
    path("sales_analysis/", sales_analysis_view, name="closed_sales_analysis"),
    path('assign-tags-to-client/', assign_tags_to_client, name='assign_tags_to_client'),
    path('tag-statistics/', tag_statistics, name='tag_statistics'),
]