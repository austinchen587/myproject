from django.contrib.auth.models import AbstractUser  # 从Django中导入AbstractUser类，用于扩展用户模型
from django.db import models


# 自定义用户模型，继承自Django内置的AbstractUser
class SalesUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', '普通用户'),
        ('group_leader', '组长'),
        ('sales_super_admin', '销售超级管理'),  # 新增角色: 销售超级管理
        ('admin', '管理员'),
        ('assistant', '助教'),
        ('assistant_leader', '助教管理'),  # 修改角色: 助教管理
        ('hr', '人事'),  # 新增角色: 人事
        ('hr_manager', '人事主管'),  # 新增角色: 人事主管
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user', verbose_name='用户角色')  # 用户角色，默认为普通用户

    # 用户的直接上级，例如组长/超级管理员
    group_leader = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='team_members',
        help_text="为该用户分配一个组长.",
        verbose_name='组长'
    )

    # 助教的直接上级是助教管理
    assistant_leader = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assistants',
        help_text="为助教分配一个助教管理.",
        verbose_name='助教管理'
    )

    # 销售超级管理的直接上级是自己，也可以对所有的 group_leader 负责
    sales_super_admin = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='leaders',
        help_text="为组长分配一个销售超级管理.",
        verbose_name='销售超级管理'
    )

    # 人事的直接上级是人事主管
    hr_manager = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='hr_team',
        help_text="为人事分配一个人事主管.",
        verbose_name='人事主管'
    )

    # 添加related_name参数，解决与默认User模型的冲突
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='salesuser_set',  # 设置反向关联的related_name，避免冲突
        blank=True,
        help_text='该用户所属的用户组',
        verbose_name='用户组',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='salesuser_set',  # 设置反向关联的related_name，避免冲突
        blank=True,
        help_text='该用户拥有的特定权限',
        verbose_name='用户权限',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'