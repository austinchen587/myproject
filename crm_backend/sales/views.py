# sales/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customerlist')  # 登录成功后重定向到 customerlist 页面
        else:
            messages.error(request, '用户名或密码错误')
    
    return render(request, 'login.html')