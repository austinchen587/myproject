# crm_backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),  # 包含 sales 应用的 URL 配置
    path('', include('customers.urls')),    # 引入 customers 应用的 URL 配置
   

]