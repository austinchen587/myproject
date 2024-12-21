from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import CustomerForm


@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.updated_by = request.user
            customer.save()
            messages.success(request, '客户添加成功')
            return redirect('customerlist')
        else:
            messages.error(request, '表单验证失败，请检查输入内容')
    else:
        form = CustomerForm()
    return render(request, 'add_customer/add_customer.html', {'form': form})