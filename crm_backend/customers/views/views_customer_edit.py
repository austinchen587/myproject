from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Customer
from ..forms import CustomerForm
from django.contrib import messages
from django.http import JsonResponse

@login_required
def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "客户信息更新成功！")
            return redirect('customerlist')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'edit_customer/edit_customer.html', {'form': form, 'customer': customer})


@login_required
def update_customer(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': '表单无效'})
    return JsonResponse({'success': False, 'message': '仅支持POST请求'})