from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesUserViewSet, login_view,current_user,RegisterUserView
from rest_framework_simplejwt.views import TokenRefreshView
from customers.views import CustomerViewSet

router = DefaultRouter()
router.register(r'sales', SalesUserViewSet)  # 改为 'users'，因为ViewSet是针对用户的
router.register(r'customers', CustomerViewSet)  # 确保客户路由已经注册

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),  # 确保 URL 匹配正确
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('customers/', include('customers.urls')),
    path('current-user/', current_user, name='current-user'),
    path('register/', RegisterUserView.as_view(), name='register'),
]