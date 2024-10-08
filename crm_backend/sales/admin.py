from django.contrib import admin
from .models import SalesUser
from django.contrib.auth.admin import UserAdmin

@admin.register(SalesUser)
class SalesUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'is_active','is_superuser')
    list_filter = ('role', 'is_active')
    search_fields = ('username','role')


    # 确保在创建或修改用户时显示密码修改表单
    change_password_form = UserAdmin.change_password_form

    def save_model(self, request, obj, form, change):
        # 如果是新创建用户或者密码有变动
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)