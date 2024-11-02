# sales/urls.py

from django.urls import path
from .views import login_view, home

urlpatterns = [
    path('', home, name='home'),  # 根路径为home页面
    path('login/', login_view, name='login'),

]