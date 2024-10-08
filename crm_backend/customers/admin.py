from django.contrib import admin
from .models import Customer
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth import get_user_model

# 获取用户模型
User = get_user_model()

class CustomerResource(resources.ModelResource):
    # 明确指定id字段
    id = fields.Field(column_name='id', attribute='id')

    # 处理外键字段的显示（如created_by, updated_by）
    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(User, 'username')  # 用username显示创建人
    )
    
    updated_by = fields.Field(
        column_name='updated_by',
        attribute='updated_by',
        widget=ForeignKeyWidget(User, 'username')  # 用username显示修改人
    )

    class Meta:
        model = Customer
        fields = (
            'id', 'name', 'phone', 'education', 'major_category', 'status', 'address', 
            'city', 'intention', 'is_closed', 'is_invited', 'is_joined', 
            'data_source', 'attended_first_live', 'attended_second_live', 
            'first_day_watch_duration', 'second_day_watch_duration', 'created_by', 
            'updated_by', 'created_at', 'updated_at', 'description'
        )
        export_order = fields


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource  # 设置导入导出资源
    list_display = ('name', 'phone','created_by', 'intention','is_invited','is_joined','is_closed', 'attended_first_live', 'attended_second_live','created_at')
    search_fields = ('name', 'phone','data_source')
    list_filter = ('is_closed', 'attended_first_live', 'attended_second_live')