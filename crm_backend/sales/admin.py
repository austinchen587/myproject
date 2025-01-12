from django.contrib import admin
from .models import SalesUser
from django.contrib.auth.admin import UserAdmin

@admin.register(SalesUser)
class SalesUserAdmin(admin.ModelAdmin):
    # 显示列表中的字段
    list_display = (
        'username', 'role', 'get_status_display', 'group_leader', 
        'assistant_leader', 'sales_super_admin', 'hr_manager', 'is_active', 'is_superuser'
    )
    list_filter = ('role', 'status', 'is_active')  # 按角色、状态和激活状态过滤
    search_fields = ('username', 'role')  # 支持搜索

    # 确保在创建或修改用户时显示密码修改表单
    change_password_form = UserAdmin.change_password_form

    # 自定义保存逻辑
    def save_model(self, request, obj, form, change):
        # 如果是新创建用户或者密码有变动
        if 'password' in form.cleaned_data and form.cleaned_data['password']:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    # 增强表单显示，新增字段对应于模型的新增字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('个人信息', {'fields': ('first_name', 'last_name', 'email')}),
        ('角色与权限', {'fields': ('role', 'status', 'group_leader', 'assistant_leader', 'sales_super_admin', 'hr_manager')}),
        ('状态', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('组与权限', {'fields': ('groups', 'user_permissions')}),
    )