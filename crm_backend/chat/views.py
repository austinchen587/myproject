from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated  # 如果你需要认证
import requests
from django.views.decorators.csrf import csrf_protect  # 确保 CSRF 保护

# 渲染聊天界面
def chat_view(request):
    return render(request, 'chat/chat.html')

# 外部 API 配置
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
API_KEY = "sk-93bd1beb96d2486f987f3efc2f7b0a04"  # 你自己的 API Key

@csrf_protect  # 确保启用 CSRF 保护
@api_view(['POST'])
def chat_api(request):
    user_message = request.data.get('message')

    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)

    # 调用外部聊天 API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }
    payload = {
        "model": "qwen-plus",  # 选择合适的模型
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response_data = response.json()
        reply = response_data.get('choices')[0].get('message').get('content')

        return JsonResponse({'reply': reply})

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)