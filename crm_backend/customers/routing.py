from django.urls import re_path
from .consumers import CustomerCommentConsumer  # 你的 WebSocket 处理器

websocket_urlpatterns = [
    re_path(r"ws/comments/$", CustomerCommentConsumer.as_asgi()),  # WebSocket 路由
]