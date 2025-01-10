from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # 显示列表页面的字段
    list_display = (
        'name', 'department', 'position', 'id_card_number', 
        'gender', 'age', 'phone_number', 'education', 'marital_status', 
        'entry_date', 'status'
    )
    
    # 添加过滤器
    list_filter = ('department', 'position', 'gender', 'education', 'status', 'marital_status')
    
    # 可搜索的字段
    search_fields = ('name', 'id_card_number', 'phone_number', 'department', 'position')
    
    # 排序
    ordering = ('entry_date',)
    
    # 每页显示的记录数
    list_per_page = 25

    # 显示详情页面的字段布局
    fieldsets = (
        ("基础信息", {
            'fields': ('name', 'gender', 'age', 'birth_date', 'phone_number', 'native_place', 'marital_status')
        }),
        ("职位信息", {
            'fields': ('department', 'position', 'entry_date', 'seniority_days', 'status')
        }),
        ("合同信息", {
            'fields': ('labor_contract_type', 'contract_start_date', 'contract_end_date')
        }),
        ("离职信息", {
            'fields': ('last_working_day', 'resignation_reason')
        }),
    )