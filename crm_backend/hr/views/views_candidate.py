from django.core.paginator import Paginator
from django.shortcuts import render
from hr.models import Candidate

def candidate_list(request):
    candidates = Candidate.objects.all().order_by('-interview_date')  # 按面试时间降序排序
    paginator = Paginator(candidates, 20)  # 每页显示 20 条数据
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'hr/hr_candidate.html', {'candidates': page_obj})