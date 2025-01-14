from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Candidate


def add_candidate(request):
    if request.method == "POST":
        try:
            # 提交数据时，字段为空则使用模型默认值
            candidate = Candidate(
                interview_date=request.POST.get("interview_date") or None,
                candidate_name=request.POST.get("candidate_name") or "",
                job_position=request.POST.get("job_position") or "",
                gender=request.POST.get("gender") or "未知",
                phone_number=request.POST.get("phone_number") or "",
                age=request.POST.get("age") if request.POST.get("age") else None,
                marital_status=request.POST.get("marital_status") or "未知",
                has_sales_experience=request.POST.get("has_sales_experience") == "是" if request.POST.get("has_sales_experience") else False,
                initial_interviewer=request.POST.get("initial_interviewer") or "",
                final_interviewer=request.POST.get("final_interviewer") or "",
                interview_result=request.POST.get("interview_result") or "未定",
                rejection_reason=request.POST.get("rejection_reason") or "",
                inviter=request.POST.get("inviter") or "",
                invitation_channel=request.POST.get("invitation_channel") or "",
                is_employed=request.POST.get("is_employed") == "是" if request.POST.get("is_employed") else False,
                employment_date=request.POST.get("employment_date") or None,
                passed_3_day_trial=request.POST.get("passed_3_day_trial") == "是" if request.POST.get("passed_3_day_trial") else False,
                tracking_1_month=request.POST.get("tracking_1_month") or "",
                tracking_3_months=request.POST.get("tracking_3_months") or "",
            )
            candidate.save()
            messages.success(request, "候选人信息已成功添加！")
        except Exception as e:
            messages.error(request, f"添加候选人信息时出错：{e}")
        return redirect("hr:candidate_list")
    return render(request, "hr/candidate_add.html")