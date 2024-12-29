from django.urls import path
from .views import library_dashboard, upload_file, manage_tags, update_tags, search_files, manage_files,edit_file,delete_file,view_file,delete_tag

app_name = 'library'

urlpatterns = [
    path('', library_dashboard, name='dashboard'),  # 修改路由名称为 library_dashboard
    path('upload/', upload_file, name='upload_file'),
    path('tags/manage/', manage_tags, name='manage_tags'),
    path('tags/update/<int:tag_id>/', update_tags, name='update_tags'),
    path('search/', search_files, name='search_files'),  # 确保添加了搜索路由
    path('files/manage/', manage_files, name='manage_files'),  # 新增文件管理路由
    path('files/edit/<int:file_id>/', edit_file, name='edit_file'),
    path('files/delete/<int:file_id>/', delete_file, name='delete_file'),
    path('files/view/<int:file_id>/', view_file, name='view_file'),
    path('tags/delete/<int:tag_id>/', delete_tag, name='delete_tag'),
]