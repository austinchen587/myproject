from django.db import models

class Tag(models.Model):
    """
    标签模型：支持多级嵌套结构
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名称")
    description = models.TextField(blank=True, null=True, verbose_name="标签描述")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name="父标签"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签管理"
        ordering = ['name']  # 默认按名称排序

    def __str__(self):
        """
        以层级结构显示标签
        """
        if self.parent:
            return f"{self.parent} -> {self.name}"
        return self.name

    def get_full_path(self):
        """
        递归获取标签的全路径（包括所有上级标签）
        """
        if self.parent:
            return f"{self.parent.get_full_path()} > {self.name}"
        return self.name

    @property
    def level(self):
        """
        获取标签层级（从0开始，顶级标签为0级）
        """
        level = 0
        current = self.parent
        while current:
            level += 1
            current = current.parent
        return level

    @property
    def child_count(self):
        """
        获取当前标签的直接子标签数量
        """
        return self.children.count()

    @property
    def all_descendants(self):
        """
        获取所有子标签，包括递归的子标签
        """
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.all_descendants)
        return descendants

class LibraryFile(models.Model):
    """
    文件模型：
    - 存储文件信息。
    - 支持关联多个标签。
    """
    name = models.CharField(max_length=255, verbose_name="文件名")  # 文件名
    file = models.FileField(upload_to='library/', max_length=255, verbose_name="文件路径")  # 文件路径（存储在 OSS）
    tags = models.ManyToManyField(Tag, related_name='files', verbose_name="标签")  # 多对多关联标签
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")  # 文件上传时间

    class Meta:
        verbose_name = "文件"
        verbose_name_plural = "文件"
        ordering = ['-uploaded_at']  # 文件按照上传时间倒序排序

    def __str__(self):
        return self.name