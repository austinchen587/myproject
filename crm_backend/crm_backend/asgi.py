"""
ASGI config for crm_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import customers.routing  # 替换为你的 WebSocket 路由模块

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_backend.settings')

# ASGI 应用配置，支持 HTTP 和 WebSockets
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 处理普通 HTTP 请求
    "websocket": AuthMiddlewareStack(  # 处理 WebSocket 连接
        URLRouter(
            customers.routing.websocket_urlpatterns  # WebSocket 路由
        )
    ),
})