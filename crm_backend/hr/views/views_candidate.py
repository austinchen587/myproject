from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Candidate

def candidate_list(request):
    # 获取筛选参数
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    candidate_name = request.GET.get('candidate_name')
    phone_number = request.GET.get('phone_number')
    invitation_channel = request.GET.get('invitation_channel')
    interview_result = request.GET.get('interview_result')

    # 初始查询集
    candidates = Candidate.objects.all().order_by('-interview_date')

    # 日期筛选
    if start_date:
        candidates = candidates.filter(interview_date__gte=start_date)
    if end_date:
        candidates = candidates.filter(interview_date__lte=end_date)

    # 字段筛选
    if candidate_name:
        candidates = candidates.filter(candidate_name__icontains=candidate_name)
    if phone_number:
        candidates = candidates.filter(phone_number__icontains=phone_number)
    if invitation_channel:
        candidates = candidates.filter(invitation_channel__icontains=invitation_channel)
    if interview_result:
        candidates = candidates.filter(interview_result__icontains=interview_result)

    # 分页
    paginator = Paginator(candidates, 20)  # 每页显示 20 条记录
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hr/hr_candidate.html', {'candidates': page_obj})