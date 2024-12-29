from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibraryFileForm, TagForm
from .models import LibraryFile, Tag
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test

# 定义检查是否为管理员用户的函数
def is_admin(user):
    """检查用户是否为管理员"""
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def upload_file(request):
    """上传文件并打标签（仅管理员）"""
    if request.method == 'POST':
        form = LibraryFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:upload_file')
    else:
        form = LibraryFileForm()

    return render(request, 'library/upload_file.html', {'form': form})

@user_passes_test(is_admin)
def manage_tags(request):
    """
    管理标签视图
    """
    tags = Tag.objects.filter(parent=None)  # 查询所有顶级标签
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:manage_tags')
    else:
        form = TagForm()

    return render(request, 'library/manage_tags.html', {'form': form, 'tags': tags})



@user_passes_test(is_admin)
def update_tags(request, tag_id):
    """更新标签（仅管理员）"""
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('library:manage_tags')
    else:
        form = TagForm(instance=tag)

    return render(request, 'library/update_tag.html', {'form': form})

def library_dashboard(request):
    """资料库主页"""
    return render(request, 'library/library_dashboard.html')

def search_files(request):
    """搜索文件（普通用户和管理员都可用）"""
    query = request.GET.get('q', '')  # 获取用户输入的搜索关键词
    if query:
        # 检索文件名、标签名或描述中包含关键词的文件
        results = LibraryFile.objects.filter(
            Q(name__icontains=query) |  # 文件名包含关键词
            Q(tags__name__icontains=query)  # 标签名包含关键词
        ).distinct()  # 去重
    else:
        results = LibraryFile.objects.all()  # 如果没有关键词，显示所有文件

    return render(request, 'library/search/search_results.html', {'results': results, 'query': query})

@user_passes_test(is_admin)
def manage_files(request):
    """管理文件（仅管理员）"""
    files = LibraryFile.objects.all()  # 获取所有上传的文件
    return render(request, 'library/manage_files.html', {'files': files})