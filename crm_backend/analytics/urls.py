# analytics/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomerAnalysisViewSet

# 创建一个默认的路由器
router = DefaultRouter()

# 注册 CustomerAnalysisViewSet 的路由
router.register(r'customer-analysis', CustomerAnalysisViewSet, basename='customer-analysis')

urlpatterns = [
    # 使用 router 自动生成的路由
    path('', include(router.urls)),
]