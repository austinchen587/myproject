from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import SalesUser  # 假设你的 User 模型在该文件中

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 检查用户状态
            if user.status == 'active':
                login(request, user)
                return redirect('dashboard')  # 登录成功后重定向到选择页面
            else:
                messages.error(request, '账户已离职，无法登录')  # 如果是离职状态，提示信息
        else:
            messages.error(request, '用户名或密码错误')
    
    return render(request, 'login.html')