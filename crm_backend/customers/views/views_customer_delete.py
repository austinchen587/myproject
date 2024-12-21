from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import Customer


@login_required
def delete_customer(request, customer_id):  # 参数名应与路由一致
    if request.method == "POST":
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return JsonResponse({"success": True, "message": "客户删除成功"})
    return JsonResponse({"success": False, "message": "无效请求"})