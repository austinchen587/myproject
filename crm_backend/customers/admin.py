from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Customer

class CustomerResource(resources.ModelResource):

    class Meta:
        model = Customer
        # 导入models.py定义的所有字段
        fields = (
            'id', 'name', 'phone', 'education', 'major_category', 'status', 
            'student_batch', 'address', 'city', 'intention', 
            'customer_needs_analysis', 'customer_personality_analysis', 
            'cloud_computing_promotion_content', 'is_closed', 'is_invited', 'is_joined', 
            'is_contacted', 'is_wechat_added', 'wechat_name', 'data_source', 
            'attended_first_live', 'attended_second_live', 
            'first_day_watch_duration', 'second_day_watch_duration', 
            'first_day_feedback', 'second_day_feedback', 'persona_chat', 
            'additional_students', 'comments_count', 
            'deal_7_days_checked', 'deal_7_days_text', 
            'deal_14_days_checked', 'deal_14_days_text', 
            'deal_21_days_checked', 'deal_21_days_text', 
            'is_course_reminder', 'created_by', 'updated_by', 
            'created_at', 'updated_at', 'description'
        )
        # 配置导入选项
        import_id_fields = ['id']
        skip_unchanged = True  # 跳过没有变更的行
        report_skipped = True  # 报告跳过的行

# 在admin界面中注册模型和资源
@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ('name', 'phone', 'education', 'major_category', 'status', 'city', 'is_closed')
    search_fields = ('name', 'phone', 'city')
    list_filter = ('education', 'status', 'is_closed')