from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import ClientData
from decimal import Decimal, InvalidOperation


def add_client(request):
    if request.method == "POST":
        try:
            # 获取手动输入的日期
            registration_date = request.POST.get("registration_date")
            if not registration_date:
                raise ValueError("注册日期是必填项")  # 如果没有提供日期，抛出异常

            # 自动获取当前操作用户的用户名作为负责人
            responsible_person = request.user.username if request.user.is_authenticated else "未知"

            # 获取并处理表单数据
            source_channel = request.POST.get("source_channel") or "未知"
            name = request.POST.get("name") or "未知"
            gender = request.POST.get("gender") or "未知"
            age = request.POST.get("age") or "未知"
            education = request.POST.get("education") or "未知"
            major = request.POST.get("major") or "未知"
            employment_status = request.POST.get("employment_status") or "未知"
            phone = request.POST.get("phone") or "未知"
            sales_teacher = request.POST.get("sales_teacher") or "未知"
            follow_up_record = request.POST.get("follow_up_record") or "无记录"
            problem_exists = request.POST.get("problem_exists") or "无问题"
            solution = request.POST.get("solution") or "无解决方案"
            remarks = request.POST.get("remarks") or "无备注"
            deal_status = request.POST.get("deal_status") or "未知"
            payment_method = request.POST.get("payment_method") or "未知"
            customer_summary = request.POST.get("customer_summary") or "无总结"

            # 处理支付金额
            try:
                payment_amount = Decimal(request.POST.get("payment_amount")) if request.POST.get("payment_amount") else None
            except InvalidOperation:
                payment_amount = None

            # 创建新的 ClientData 对象
            ClientData.objects.create(
                registration_date=registration_date,  # 使用手动输入的日期
                source_channel=source_channel,
                name=name,
                gender=gender,
                age=age,
                education=education,
                major=major,
                employment_status=employment_status,
                phone=phone,
                sales_teacher=sales_teacher,
                follow_up_record=follow_up_record,
                problem_exists=problem_exists,
                solution=solution,
                remarks=remarks,
                deal_status=deal_status,
                payment_method=payment_method,
                payment_amount=payment_amount,
                customer_summary=customer_summary,
                responsible_person=responsible_person,  # 自动添加负责人
            )

            # 跳转到客户列表页面
            return redirect(reverse("closed:client_data_list"))  # 假设 client_data_list 是客户列表的 URL name

        except Exception as e:
            # 捕获异常并传递到模板中
            return render(request, "closed/closed_add.html", {"error": str(e)})

    return render(request, "closed/closed_add.html")