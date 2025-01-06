from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from ..models import LibraryFile
from ..forms import LibraryFileForm
from ..models import LibraryFile,Tag
from django.core.paginator import Paginator

# 检查用户是否为管理员
def is_admin(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin) 
def manage_files(request):
    """
    管理文件视图，支持分页和标签筛选
    """
    tag_filter = request.GET.get('tag')  # 获取筛选标签
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页

    # 如果指定了标签筛选，筛选出对应文件，否则显示所有文件
    if tag_filter:
        files = LibraryFile.objects.filter(tags__id=tag_filter).distinct().order_by('-uploaded_at')
    else:
        files = LibraryFile.objects.all().order_by('-uploaded_at')

    # 设置分页，每页显示 5 个文件
    paginator = Paginator(files, 5)
    files = paginator.get_page(page)

    # 查询所有顶级标签并预加载子标签
    all_tags = Tag.objects.filter(parent=None).prefetch_related('children')

    return render(request, 'library/manage_files/manage_files.html', {
        'files': files,
        'all_tags': all_tags,
        'tag_filter': tag_filter,
    })

@user_passes_test(is_admin)
def edit_file(request, file_id):
    """
    编辑文件视图
    """
    library_file = get_object_or_404(LibraryFile, id=file_id)
    if request.method == 'POST':
        form = LibraryFileForm(request.POST, request.FILES, instance=library_file)
        if form.is_valid():
            form.save()
            return redirect('library:manage_files')
    else:
        form = LibraryFileForm(instance=library_file)
    return render(request, 'library/manage_files/edit_file.html', {'form': form, 'file': library_file})

@user_passes_test(is_admin)
def delete_file(request, file_id):
    """
    删除文件视图
    """
    library_file = get_object_or_404(LibraryFile, id=file_id)
    if request.method == 'POST':
        library_file.delete()
        return redirect('library:manage_files')
    return render(request, 'library/manage_files/delete_file.html', {'file': library_file})


def view_file(request, file_id):
    """
    查看文件详情
    """
    file_obj = get_object_or_404(LibraryFile, id=file_id)
    return render(request, 'library/manage_files/view_file.html', {'file': file_obj})