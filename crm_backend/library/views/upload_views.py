from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from ..forms import LibraryFileForm
from ..models import Tag

# 检查用户是否为管理员
def is_admin(user):
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

    tags = Tag.objects.prefetch_related('children').filter(parent=None)  # 查询顶级标签
    print("Tags in view:", tags)  # 打印调试信息
    return render(request, 'library/upload_file.html', {
        'form': form,
        'tags': tags,  # 传递到模板
    })