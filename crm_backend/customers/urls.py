from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, add_customer

# 初始化路由器
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')  # 注册 ViewSet 路由

urlpatterns = [
    #path('list/', get_customers, name='get_customers'),  # get_customers 视图
    path('add/', add_customer, name='add_customer'),     # POST 请求添加客户数据
    path('', include(router.urls)),  # 使用 router 自动生成的 ViewSet 路由
]