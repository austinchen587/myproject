from django.urls import path
from .views import chat_view, chat_api

urlpatterns = [
    path('', chat_view, name='chat_view'),  # 访问 /chat 时加载聊天页面
    path('api/', chat_api, name='chat_api'),  # API 请求接口
]