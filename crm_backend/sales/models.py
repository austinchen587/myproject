from django.contrib.auth.models import AbstractUser
from django.db import models

# 自定义用户模型
class SalesUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', '普通用户'),
        ('group_leader', '组长'),
        ('sales_super_admin', '销售超级管理'),
        ('admin', '管理员'),
        ('assistant', '助教'),
        ('assistant_leader', '助教管理'),
        ('hr', '人事'),
        ('hr_manager', '人事主管'),
    ]

    STATUS_CHOICES = [
        ('active', '在职'),
        ('inactive', '离职'),
    ]

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='用户角色'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='用户状态',
        help_text='标记用户是当前在职还是离职'
    )

    group_leader = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='team_members',
        help_text="为该用户分配一个组长.",
        verbose_name='组长'
    )

    assistant_leader = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assistants',
        help_text="为助教分配一个助教管理.",
        verbose_name='助教管理'
    )

    sales_super_admin = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='leaders',
        help_text="为组长分配一个销售超级管理.",
        verbose_name='销售超级管理'
    )

    hr_manager = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='hr_team',
        help_text="为人事分配一个人事主管.",
        verbose_name='人事主管'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='salesuser_set',
        blank=True,
        help_text='该用户所属的用户组',
        verbose_name='用户组',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='salesuser_set',
        blank=True,
        help_text='该用户拥有的特定权限',
        verbose_name='用户权限',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'