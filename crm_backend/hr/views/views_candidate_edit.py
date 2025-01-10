from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Candidate

def update_candidate(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    if request.method == 'POST':
        try:
            candidate.interview_date = request.POST.get('interview_date')
            candidate.candidate_name = request.POST.get('candidate_name')
            candidate.job_position = request.POST.get('job_position')
            candidate.gender = request.POST.get('gender')
            candidate.phone_number = request.POST.get('phone_number')
            candidate.age = request.POST.get('age') or None
            candidate.marital_status = request.POST.get('marital_status')
            candidate.has_sales_experience = request.POST.get('has_sales_experience') == "是"
            candidate.initial_interviewer = request.POST.get('initial_interviewer')
            candidate.final_interviewer = request.POST.get('final_interviewer')
            candidate.interview_result = request.POST.get('interview_result')
            candidate.rejection_reason = request.POST.get('rejection_reason')
            candidate.inviter = request.POST.get('inviter')
            candidate.invitation_channel = request.POST.get('invitation_channel')
            candidate.is_employed = request.POST.get('is_employed') == "是"
            candidate.employment_date = request.POST.get('employment_date') or None
            candidate.passed_3_day_trial = request.POST.get('passed_3_day_trial') == "是"
            candidate.tracking_1_month = request.POST.get('tracking_1_month')
            candidate.tracking_3_months = request.POST.get('tracking_3_months')
                    # 处理上传的图片
            if 'photo' in request.FILES:
                candidate.photo = request.FILES['photo']

            candidate.save()
            messages.success(request, '更新成功！')
        except Exception as e:
            messages.error(request, f'更新失败: {str(e)}')
        return redirect('hr:candidate_list')
    return render(request, 'hr/candidate_edit.html', {'candidate': candidate})


def delete_candidate(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    try:
        candidate.delete()
        messages.success(request, '删除成功！')
    except Exception as e:
        messages.error(request, f'删除失败: {str(e)}')
    return redirect('hr:candidate_list')