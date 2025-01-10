from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Candidate

def add_candidate(request):
    if request.method == "POST":
        try:
            candidate = Candidate(
                interview_date=request.POST.get('interview_date'),
                candidate_name=request.POST.get('candidate_name'),
                job_position=request.POST.get('job_position'),
                gender=request.POST.get('gender'),
                phone_number=request.POST.get('phone_number'),
                age=request.POST.get('age') if request.POST.get('age') else None,
                marital_status=request.POST.get('marital_status'),
                has_sales_experience=request.POST.get('has_sales_experience') == "是",
                initial_interviewer=request.POST.get('initial_interviewer'),
                final_interviewer=request.POST.get('final_interviewer'),
                interview_result=request.POST.get('interview_result'),
                rejection_reason=request.POST.get('rejection_reason'),
                inviter=request.POST.get('inviter'),
                invitation_channel=request.POST.get('invitation_channel'),
                is_employed=request.POST.get('is_employed') == "是",
                employment_date=request.POST.get('employment_date') if request.POST.get('employment_date') else None,
                passed_3_day_trial=request.POST.get('passed_3_day_trial') == "是",
                tracking_1_month=request.POST.get('tracking_1_month'),
                tracking_3_months=request.POST.get('tracking_3_months')
            )
            candidate.save()
            messages.success(request, "候选人信息已成功添加！")
        except Exception as e:
            messages.error(request, f"添加候选人信息时出错：{e}")
        return redirect('hr:candidate_list')
    return render(request, 'hr/candidate_add.html')