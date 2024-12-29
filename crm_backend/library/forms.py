from django import forms
from .models import LibraryFile, Tag


class LibraryFileForm(forms.ModelForm):
    """
    文件上传和标签关联表单
    """
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.none(),  # 初始为空，通过动态加载
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input stylish-checkbox',
        }),
        label="标签",
        help_text="选择一个或多个标签（支持多层级）。"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
        self.fields['tags'].choices = self._get_hierarchical_tags()

    def _get_hierarchical_tags(self):
        """
        获取层级结构的标签列表，包含缩进
        """
        def build_choices(tag, level=0):
            prefix = "—" * level  # 使用 `—` 表示层级缩进
            choices = [(tag.id, f"{prefix} {tag.name} - {tag.description or '无描述'}")]
            for child in tag.children.all().order_by('name'):  # 按名称排序
                choices += build_choices(child, level + 1)
            return choices

        hierarchical_choices = []
        for top_tag in Tag.objects.filter(parent=None).order_by('name'):
            hierarchical_choices += build_choices(top_tag)
        return hierarchical_choices

    class Meta:
        model = LibraryFile
        fields = ['name', 'file', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control stylish-input',
                'placeholder': '请输入文件名',
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control stylish-file-input',
            }),
        }
        labels = {
            'name': '文件名',
            'file': '文件',
            'tags': '标签',
        }
        help_texts = {
            'name': '为文件提供一个简洁的文件名。',
            'file': '请选择要上传的文件。',
        }


class TagForm(forms.ModelForm):
    """
    标签管理表单，支持动态多级父标签选择
    """
    parent = forms.ChoiceField(
        required=False,
        label="父标签",
        widget=forms.Select(attrs={
            'class': 'form-control stylish-select',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 动态设置父标签选项
        tag_choices = [("", "无（顶级标签）")]
        for tag in Tag.objects.filter(parent=None):  # 从顶级标签开始
            self._add_tag_hierarchy(tag_choices, tag, 0)
        self.fields['parent'].choices = tag_choices

    def _add_tag_hierarchy(self, tag_choices, tag, level):
        """
        递归添加标签层级选项
        """
        tag_choices.append((str(tag.id), f"{'--' * level} {tag.name}"))
        for child in tag.children.all():
            self._add_tag_hierarchy(tag_choices, child, level + 1)

    def clean_parent(self):
        """
        清理并转换 `parent` 值为 `Tag` 实例
        """
        parent_id = self.cleaned_data.get('parent')
        if parent_id:
            try:
                return Tag.objects.get(id=parent_id)
            except Tag.DoesNotExist:
                raise forms.ValidationError("选择的父标签不存在。")
        return None  # 如果没有选择父标签，返回 None

    class Meta:
        model = Tag
        fields = ['name', 'description', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control stylish-input',
                'placeholder': '请输入标签名称',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control stylish-textarea',
                'placeholder': '请输入标签描述',
                'rows': 3,
            }),
        }
        labels = {
            'name': '标签名称',
            'description': '标签描述',
            'parent': '父标签'
        }
        help_texts = {
            'parent': '如果该标签是子标签，请选择对应的父标签。',
        }