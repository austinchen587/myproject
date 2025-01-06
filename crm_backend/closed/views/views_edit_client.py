from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..models import ClientData
from datetime import datetime
from decimal import Decimal, InvalidOperation

# 更新客户信息
def update_client(request, client_id):
    client = get_object_or_404(ClientData, id=client_id)

    if request.method == "POST":
        try:
            # 更新表单数据
            client.registration_date = request.POST.get("registration_date")
            client.source_channel = request.POST.get("source_channel") or "未知"
            client.name = request.POST.get("name") or "未知"
            client.gender = request.POST.get("gender") or "未知"
            client.age = request.POST.get("age") or "未知"
            client.education = request.POST.get("education") or "未知"
            client.major = request.POST.get("major") or "未知"
            client.employment_status = request.POST.get("employment_status") or "未知"
            client.phone = request.POST.get("phone") or "未知"
            client.sales_teacher = request.POST.get("sales_teacher") or "未知"
            client.follow_up_record = request.POST.get("follow_up_record") or "无记录"
            client.problem_exists = request.POST.get("problem_exists") or "无问题"
            client.solution = request.POST.get("solution") or "无解决方案"
            client.remarks = request.POST.get("remarks") or "无备注"
            client.deal_status = request.POST.get("deal_status") or "未知"
            client.payment_method = request.POST.get("payment_method") or "未知"

            try:
                client.payment_amount = Decimal(request.POST.get("payment_amount")) if request.POST.get("payment_amount") else None
            except InvalidOperation:
                client.payment_amount = None

            client.customer_summary = request.POST.get("customer_summary") or "无总结"

            # 保存更新
            client.save()

            return redirect(reverse("closed:client_data_list"))
        except Exception as e:
            print(f"Error occurred: {e}")
            return render(request, "closed/closed_update.html", {"client": client, "error": str(e)})

    return render(request, "closed/closed_update.html", {"client": client})


# 删除客户信息
def delete_client(request, client_id):
    client = get_object_or_404(ClientData, id=client_id)

    if request.method == "POST":
        client.delete()
        return redirect(reverse("closed:client_data_list"))

    return render(request, "closed/closed_delete_confirm.html", {"client": client})