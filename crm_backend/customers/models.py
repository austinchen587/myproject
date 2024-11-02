from django.db import models
from sales.models import SalesUser

# 定义客户模型
class Customer(models.Model):
    name = models.CharField(max_length=100, default='未知', verbose_name='姓名')
    phone = models.CharField(max_length=20, verbose_name='电话')
    education = models.CharField(max_length=20, choices=[
        ('大专以下', '大专以下'),
        ('大专', '大专'),
        ('本科', '本科'),
        ('研究生及以上', '研究生及以上'),
        ('未知', '未知'),
    ], default='大专', verbose_name='学历')
    major_category = models.CharField(max_length=10, choices=[
        ('IT', 'IT'),
        ('非IT', '非IT'),
        ('未知', '未知'),
    ], default='IT', verbose_name='专业类别')
    status = models.CharField(max_length=15, choices=[
        ('在职', '在职'),
        ('待业', '待业'),
        ('未知', '未知'),
    ], default='待业', verbose_name='状态')
    student_batch = models.CharField(max_length=20, default='0', verbose_name='期期学员')

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='就业意向城市')
    city = models.CharField(max_length=255, default='Default City', verbose_name='当前所在城市')
    intention = models.CharField(max_length=20, choices=[
        ('低', '低'),
        ('中', '中'),
        ('高', '高'),
        ('未知', '未知'),
    ], default='低', verbose_name='意向程度')

    # 允许为空的 JSON 字段
    customer_needs_analysis = models.JSONField(default=list, blank=True, null=True, verbose_name='客户挖需分析')
    customer_personality_analysis = models.JSONField(default=list, blank=True, null=True, verbose_name='客户性格分析')
    cloud_computing_promotion_content = models.JSONField(default=list, blank=True, null=True, verbose_name='云计算推广内容')

    is_closed = models.BooleanField(default=False, verbose_name='是否成交')
    is_invited = models.BooleanField(default=False, verbose_name='是否邀约')
    is_joined = models.BooleanField(default=False, verbose_name='是否入群')
    is_contacted = models.BooleanField(default=False, verbose_name='是否接通')
    is_wechat_added = models.BooleanField(default=False, verbose_name='是否加微信')

    data_source = models.CharField(max_length=100, choices=[
        ('AI数据', 'AI数据'),
        ('视频号', '视频号'),
        ('其他', '其他'),
    ], default='AI数据', verbose_name='数据来源')

    wechat_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='客户微信名')

    attended_first_live = models.BooleanField(default=False, verbose_name='参加第一天直播')
    attended_second_live = models.BooleanField(default=False, verbose_name='参加第二天直播')
    first_day_watch_duration = models.IntegerField(default=0, verbose_name='第一天观看时长')
    second_day_watch_duration = models.IntegerField(default=0, verbose_name='第二天观看时长')

    first_day_feedback = models.CharField(max_length=20, choices=[
        ('满意', '满意'),
        ('一般', '一般'),
        ('不考虑', '不考虑'),
    ], default='一般', verbose_name='第一天观后反馈')

    second_day_feedback = models.CharField(max_length=20, choices=[
        ('满意', '满意'),
        ('一般', '一般'),
        ('不考虑', '不考虑'),
    ], default='一般', verbose_name='第二天观后反馈')

    persona_chat = models.BooleanField(default=False, verbose_name='是否进行人设聊天')
    additional_students = models.BooleanField(default=False, verbose_name='是否有马甲加学员')
    comments_count = models.BooleanField(default=False, verbose_name='是否有评论')

    deal_7_days_checked = models.BooleanField(default=False, verbose_name='7天成交')
    deal_7_days_text = models.TextField(blank=True, null=True, verbose_name='7天成交说明')

    deal_14_days_checked = models.BooleanField(default=False, verbose_name='14天成交')
    deal_14_days_text = models.TextField(blank=True, null=True, verbose_name='14天成交说明')

    deal_21_days_checked = models.BooleanField(default=False, verbose_name='21天成交')
    deal_21_days_text = models.TextField(blank=True, null=True, verbose_name='21天成交说明')

    is_course_reminder = models.BooleanField(default=False, verbose_name='是否到课提醒')

    created_by = models.ForeignKey(SalesUser, on_delete=models.CASCADE, null=True, related_name='customers_created', verbose_name='创建人')
    updated_by = models.ForeignKey(SalesUser, on_delete=models.SET_NULL, null=True, related_name='customers_updated', verbose_name='最后修改人')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    description = models.TextField(blank=True, null=True, verbose_name='客户描述')

    # 增加一个主管点评字段
    supervisor_comments = models.TextField(blank=True, null=True, verbose_name='主管点评')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户列表'