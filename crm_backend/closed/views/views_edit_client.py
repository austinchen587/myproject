from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..models import ClientData
from decimal import Decimal, InvalidOperation


# 更新客户信息
def update_client(request, client_id):
    client = get_object_or_404(ClientData, id=client_id)

    if request.method == "POST":
        try:
            # 更新表单数据，不处理 `registration_date`
            client.source_channel = request.POST.get("source_channel", "未知")
            client.name = request.POST.get("name", "未知")
            client.gender = request.POST.get("gender", "未知")
            client.age = request.POST.get("age") or None
            client.education = request.POST.get("education", "未知")
            client.major = request.POST.get("major", "未知")
            client.employment_status = request.POST.get("employment_status", "未知")
            client.phone = request.POST.get("phone", "未知")
            client.sales_teacher = request.POST.get("sales_teacher", "未知")
            client.follow_up_record = request.POST.get("follow_up_record", "无记录")
            client.problem_exists = request.POST.get("problem_exists", "无问题")
            client.solution = request.POST.get("solution", "无解决方案")
            client.remarks = request.POST.get("remarks", "无备注")
            client.deal_status = request.POST.get("deal_status", "未知")
            client.payment_method = request.POST.get("payment_method", "未知")

            # 处理支付金额
            payment_str = request.POST.get("payment_amount")
            if payment_str:
                try:
                    client.payment_amount = Decimal(payment_str)
                except InvalidOperation:
                    raise ValueError("支付金额无效，请输入有效数字")

            client.customer_summary = request.POST.get("customer_summary", "无总结")

            # 保存更新
            client.save()

            return redirect(reverse("closed:client_data_list"))

        except Exception as e:
            # 捕获错误并显示
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