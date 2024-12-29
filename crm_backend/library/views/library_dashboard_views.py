from django.shortcuts import render
from ..models import Tag

def library_dashboard(request):
    # 加载顶级标签，并预加载子标签
    all_tags = Tag.objects.prefetch_related('children').filter(parent=None)

    # 获取用户选择的标签
    selected_tags = request.GET.getlist('tags')  # 获取选中的标签 ID 列表

    return render(request, 'library/library_dashboard.html', {
        'all_tags': all_tags,        # 顶级标签列表
        'selected_tags': selected_tags,  # 用户选中的标签
    })