from django.shortcuts import render
from django.db.models import Q
from ..models import LibraryFile, Tag

def search_files(request):
    """搜索文件及标签"""
    # 获取用户输入的搜索关键词和选择的标签
    query = request.GET.get('q', '').strip() if request.GET.get('q') else None
    selected_tags = request.GET.getlist('tags')  # 用户选择的标签 ID 列表

    # 初始化查询条件
    conditions = Q()
    if query:
        # 文件名或标签名包含关键词
        conditions |= Q(name__icontains=query) | Q(tags__name__icontains=query)

    if selected_tags:
        # 筛选包含用户选择的标签的文件
        conditions &= Q(tags__id__in=selected_tags)

    # 查询文件，并确保去重
    results = LibraryFile.objects.filter(conditions).distinct()

    # 获取所有顶级标签，并预加载子标签
    all_tags = Tag.objects.prefetch_related('children').filter(parent=None)

    return render(request, 'library/search/search_results.html', {
        'results': results,          # 搜索结果
        'query': query or '',        # 用户输入的关键词（避免 None）
        'selected_tags': selected_tags,  # 已选中的标签 ID
        'all_tags': all_tags,        # 顶级标签用于展示
    })