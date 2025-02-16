from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
import requests
import re

# 外部 API 配置
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
API_KEY = "sk-93bd1beb96d2486f987f3efc2f7b0a04"  # 你自己的 API Key

# 渲染聊天界面
def chat_view(request):
    return render(request, 'chat/chat.html')

@csrf_protect  # 确保启用 CSRF 保护
@api_view(['POST'])
def chat_api(request):
    user_message = request.data.get('message')

    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)

    # 获取历史对话（如果有的话）
    chat_history = request.session.get('chat_history', [])

    # 将用户消息添加到对话历史中
    chat_history.append({"role": "user", "content": user_message})

    # 保存更新后的对话历史
    request.session['chat_history'] = chat_history

    # 调用外部聊天 API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }

    # 将对话历史传递给外部 API
    payload = {
        "model": "qwen-max",  # 选择合适的模型
        "messages": chat_history  # 传递完整的对话历史作为上下文
    }

    try:
        # 发送请求到外部 API
        response = requests.post(API_URL, headers=headers, json=payload)
        response_data = response.json()

        # 获取 AI 回复
        reply = response_data.get('choices')[0].get('message').get('content')

        # 将 AI 回复添加到对话历史
        chat_history.append({"role": "assistant", "content": reply})

        # 更新会话中的对话历史
        request.session['chat_history'] = chat_history

        # 只返回 reply（不再返回 request_id）
        return JsonResponse({'reply': reply})

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)