from django.db import models
from sales.models import SalesUser
from django.core.validators import MinValueValidator
import os
from django.utils.timezone import now
from customers.storages.storages import CustomerAudioOSSStorage, CustomerImagesOSSStorage



def customer_audio_upload_path(instance, filename):
    """
    保存音频文件到 OSS 的路径。
    """
    return f"customer_audio/{instance.customer.id}/{now().strftime('%Y%m%d%H%M%S')}_{filename}"


def customer_image_upload_path(instance, filename):
    """
    保存图片文件到 OSS 的路径。
    """
    return f"customer_images/{instance.customer.id}/{now().strftime('%Y%m%d%H%M%S')}_{filename}"


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
    ], default='未知', verbose_name='学历')
    major_category = models.CharField(max_length=10, choices=[
        ('IT', 'IT'),
        ('非IT', '非IT'),
        ('未知', '未知'),
    ], default='未知', verbose_name='专业类别')
    status = models.CharField(max_length=15, choices=[
        ('在职', '在职'),
        ('待业', '待业'),
        ('未知', '未知'),
    ], default='未知', verbose_name='状态')
    #student_batch = models.CharField(max_length=20, default='0', verbose_name='期期学员')

    student_batch = models.IntegerField(
    default=0,
    verbose_name='期期学员',
    validators=[MinValueValidator(0)]
)
    

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='就业意向城市')
    city = models.CharField(max_length=255, default='未知', verbose_name='当前所在城市')
    intention = models.CharField(max_length=20, choices=[
        ('低', '低'),
        ('中', '中'),
        ('高', '高'),
        ('未知', '未知'),
    ], default='未知', verbose_name='意向程度')

    # 允许为空的 JSON 字段
    customer_needs_analysis = models.JSONField(default=list, blank=True, null=True, verbose_name='客户挖需分析')
    customer_personality_analysis = models.JSONField(default=list, blank=True, null=True, verbose_name='客户性格分析')
    cloud_computing_promotion_content = models.JSONField(default=list, blank=True, null=True, verbose_name='云计算推广内容')

    is_closed = models.BooleanField(default=False, verbose_name='是否成交')
    is_invited = models.BooleanField(default=False, verbose_name='是否感兴趣')
    is_joined = models.BooleanField(default=False, verbose_name='是否入群')
    is_contacted = models.BooleanField(default=False, verbose_name='是否接通')
    is_wechat_added = models.BooleanField(default=False, verbose_name='是否加微信')

    # 新增音频文件字段
    audio_file = models.FileField(
        upload_to=customer_audio_upload_path,  # 指定上传路径
        blank=True,
        null=True,
        verbose_name="客户音频文件"
    )

    data_source = models.CharField(max_length=100, choices=[
        ('AI数据', 'AI数据'),
        ('视频号', '视频号'),
        ('其他', '其他'),
        ('国开数据', '国开数据'),
        ('未知', '未知'),  # 新增选项
    ], default='未知', verbose_name='数据来源')

    wechat_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='客户微信名')

    attended_first_live = models.BooleanField(default=False, verbose_name='参加第一天直播')
    attended_second_live = models.BooleanField(default=False, verbose_name='参加第二天直播')
    first_day_watch_duration = models.IntegerField(default=0, verbose_name='第一天观看时长')
    second_day_watch_duration = models.IntegerField(default=0, verbose_name='第二天观看时长')

    first_day_feedback = models.CharField(max_length=20, choices=[
        ('满意', '满意'),
        ('一般', '一般'),
        ('不考虑', '不考虑'),
        ('未知', '未知'),
    ], default='未知', verbose_name='第一天观后反馈')

    second_day_feedback = models.CharField(max_length=20, choices=[
        ('满意', '满意'),
        ('一般', '一般'),
        ('不考虑', '不考虑'),
        ('未知', '未知'),
    ], default='未知', verbose_name='第二天观后反馈')

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


        # 添加一个方法获取所有评论
    def get_comments(self):
        return self.comments.all()

    # 增加一个主管点评字段
    supervisor_comments = models.TextField(blank=True, null=True, verbose_name='产品经理反馈')

    # 新增字段
    product_manager_contact = models.CharField(
        max_length=20,
        default='未分配',
        verbose_name='产品经理对接人'
    )

    # 再慎重考虑下
    reconsider_checked = models.BooleanField(default=False, verbose_name='再慎重考虑下')
    reconsider_text = models.TextField(
        blank=True,
        null=True,
        default='未知',  # 默认值设置为 "未知"
        verbose_name='再慎重考虑下说明'
    )

    # 回家商量下
    discuss_checked = models.BooleanField(default=False, verbose_name='回家商量下')
    discuss_text = models.TextField(
        blank=True,
        null=True,
        default='未知',  # 默认值设置为 "未知"
        verbose_name='回家商量下说明'
    )

    customer_level = models.CharField(
        max_length=10,  # 调整长度以支持"未知"
        choices=[
            ('A', 'A 等级'),
            ('B', 'B 等级'),
            ('未知', '未知'),
        ],
        default='未知',
        verbose_name='客户等级'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户列表'


def get_audio_storage():
    """延迟加载音频存储类"""
    return CustomerAudioOSSStorage()


def get_image_storage():
    """延迟加载图片存储类"""
    return CustomerImagesOSSStorage()


class Recording(models.Model):
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="recordings",
        verbose_name="客户"
    )
    audio_file = models.FileField(
        upload_to="customer_audio/",
        storage=get_audio_storage,  # 使用惰性加载函数
        verbose_name="录音文件",
        blank=True,  # 确保字段可为空
        null=True
    )
    image_file = models.ImageField(
        upload_to="customer_images/",
        storage=get_image_storage,  # 使用惰性加载函数
        verbose_name="图片文件",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "录音与图片记录"
        verbose_name_plural = "录音与图片记录"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer.name} ({self.created_at.strftime('%Y-%m-%d')})"
    


class Comment(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="客户"
    )
    content = models.TextField(verbose_name="评论内容")
    created_by = models.ForeignKey(
        SalesUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments_created",
        verbose_name="评论人"
    )
    created_at = models.DateTimeField(default=now, verbose_name="评论时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论记录"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer.name} 的评论 ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"