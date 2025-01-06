from django.contrib import admin
from .models import ClientData

# 创建一个 ModelAdmin 类来定制后台显示
class ClientDataAdmin(admin.ModelAdmin):
    # 在列表页中显示的字段（显示所有字段）
    list_display = [
        'name',  # 姓名
        'phone',  # 电话
        'registration_date',  # 日期   
        'source_channel',  # 来源渠道
        'gender',  # 性别
        'age',  # 年龄
        'education',  # 学历
        'major',  # 专业
        'sales_teacher',  # 就业老师
        'follow_up_record',  # 跟进记录
        'deal_status',  # 成交情况
        'payment_method',  # 支付方式
        'payment_amount',  # 支付金额
        'customer_summary',  # 客户总结
        'study_progress',  # 学习进度
    ]
    
    # 可以进行过滤的字段（为了方便筛选，可以选择几个常用的字段）
    list_filter = [
        'payment_method',  # 支付方式
        'registration_date',  # 日期
        'gender',  # 性别
        'deal_status',  # 成交情况
    ]
    
    # 可以在搜索框中搜索的字段
    search_fields = [
        'name',  # 姓名
        'phone',  # 电话
        'employment_status',  # 就业情况
        'sales_teacher',  # 就业老师
        'follow_up_record',  # 跟进记录
    ]
    
    # 排序字段，默认按报名日期排序
    ordering = ['registration_date']

# 注册模型和自定义的 ModelAdmin
admin.site.register(ClientData, ClientDataAdmin)