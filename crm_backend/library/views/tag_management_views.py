from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from ..forms import TagForm
from ..models import Tag

# 检查用户是否为管理员
def is_admin(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin)
def manage_tags(request):
    """
    管理标签（仅管理员）
    - 支持添加顶级和子标签
    - 按层级显示标签结构
    """
    tags = Tag.objects.filter(parent=None).order_by('name')  # 查询所有顶级标签并按名称排序
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "标签已成功创建！")
            return redirect('library:manage_tags')
        else:
            messages.error(request, "创建标签时发生错误，请检查表单输入。")
    else:
        form = TagForm()

    return render(request, 'library/manage_tags.html', {
        'form': form,
        'tags': tags,
    })


@user_passes_test(is_admin)
def update_tags(request, tag_id):
    """
    更新标签（仅管理员）
    - 支持更新标签名称、描述和父标签
    """
    tag = get_object_or_404(Tag, id=tag_id)  # 获取标签实例
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, f"标签 '{tag.name}' 已成功更新！")
            return redirect('library:manage_tags')
        else:
            messages.error(request, "更新标签时发生错误，请检查表单输入。")
    else:
        form = TagForm(instance=tag)

    return render(request, 'library/update_tag.html', {
        'form': form,
        'tag': tag,
    })

@user_passes_test(is_admin)
def delete_tag(request, tag_id):
    """
    删除标签（仅管理员）
    - 删除指定标签及其子标签
    """
    tag = get_object_or_404(Tag, id=tag_id)  # 获取标签实例
    if request.method == 'POST':
        tag.delete()
        messages.success(request, f"标签 '{tag.name}' 已成功删除！")
        return redirect('library:manage_tags')

    return render(request, 'library/confirm_delete_tag.html', {
        'tag': tag,
    })