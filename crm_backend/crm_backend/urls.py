# crm_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import handler404
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),  # 包含 sales 应用的 URL 配置
    path('', include('customers.urls')),    # 引入 customers 应用的 URL 配置
    path('library/', include('library.urls', namespace='library')),
    path('closed/', include('closed.urls', namespace='closed')),
    path('hr/', include('hr.urls', namespace='hr')),
    path('employee/', include('employee.urls', namespace='employee')),


]

def handle_not_found(request, exception):
    return HttpResponseNotFound("Not Found")

handler404 = "crm_backend.views.handle_not_found"