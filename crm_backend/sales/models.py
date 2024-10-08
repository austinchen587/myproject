from django.contrib.auth.models import AbstractUser # 从Django中导入AbstractUser类，用于扩展用户模型
from django.db import models
from django.utils import timezone

# 自定义用户模型，继承自Django内置的AbstractUser
class SalesUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', '普通用户'),
        ('group_leader', '组长'),
        ('admin', '管理员'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user', verbose_name='用户角色')   # 用户角色，默认为普通用户
    #group_leader = models.BooleanField(default=False)  # 是否为组长，默认不是
    group_leader = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='team_members',
        help_text="为该用户分配一个组长.",
        verbose_name='组长'
    )

    # 添加related_name参数，解决与默认User模型的冲突
    groups = models.ManyToManyField(
        'auth.Group',
        related_name = 'salesuser_set',  # 设置反向关联的related_name，避免冲突
        blank = True,
        help_text = '该用户所属的用户组',
        verbose_name = '用户组',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name = 'salesuser_set',  # 设置反向关联的related_name，避免冲突
        blank = True,
        help_text = '该用户拥有的特定权限',
        verbose_name = '用户权限',
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = '销售用户'
        verbose_name_plural = '销售用户列表'
# 作用说明：
# 该模型扩展了Django自带的用户模型，可以根据需求添加更多字段。
# 后续可以通过权限系统实现管理员和普通用户的权限区分。
