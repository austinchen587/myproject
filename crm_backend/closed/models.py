from django.db import models
from customers.models import Customer  # 确保导入 Customer 模型
from django.utils.timezone import now  # 用于获取当前日期和时间


# 路径字符串修复
from closed.storages.aliyun_storages import AliyunOSSClosedAudioStorage, AliyunOSSClosedImagesStorage


import os

def follow_up_audio_upload_path(instance, filename):
    """音频文件上传路径"""
    return os.path.join("audio", str(instance.client.id), filename)

def follow_up_image_upload_path(instance, filename):
    """图片文件上传路径"""
    return os.path.join("images", str(instance.client.id), filename)

def get_audio_storage():
    """延迟加载音频存储类"""
    return AliyunOSSClosedAudioStorage()


def get_image_storage():
    """延迟加载图片存储类"""
    return AliyunOSSClosedImagesStorage()


class ClientData(models.Model):
    """
    客户信息模型
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="客户"
    )
    registration_date = models.DateField(
        default=now,  # 自动设置为当前日期
        verbose_name="日期"
    )
    source_channel = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="来源渠道"
    )
    name = models.CharField(max_length=50, verbose_name="姓名")
    gender = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=[
            ("男", "男"),
            ("女", "女"),
            ("未知", "未知"),
        ],
        verbose_name="性别"
    )
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="年龄")
    education = models.CharField(max_length=50, null=True, blank=True, verbose_name="学历")
    major = models.CharField(max_length=50, null=True, blank=True, verbose_name="专业")
    employment_status = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        choices=[
            ("在职", "在职"),
            ("待业", "待业"),
            ("自由职业", "自由职业"),
            ("未知", "未知"),
        ],
        verbose_name="就业情况"
    )
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话")
    sales_teacher = models.CharField(max_length=50, null=True, blank=True, verbose_name="就业老师")
    follow_up_record = models.TextField(null=True, blank=True, verbose_name="跟进记录")
    problem_exists = models.TextField(null=True, blank=True, verbose_name="存在问题")
    solution = models.TextField(null=True, blank=True, verbose_name="解决办法")
    remarks = models.TextField(null=True, blank=True, verbose_name="备注")
    deal_status = models.CharField(max_length=150, null=True, blank=True, verbose_name="成交情况")
    payment_method = models.CharField(max_length=100, null=True, blank=True, verbose_name="支付方式")
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="支付金额"
    )
    customer_summary = models.TextField(null=True, blank=True, verbose_name="客户总结")
    study_progress = models.TextField(null=True, blank=True, verbose_name="学习进度")
    problem_tracking = models.TextField(null=True, blank=True, verbose_name="问题追踪")
    situation_analysis = models.TextField(null=True, blank=True, verbose_name="情况分析")
    is_employed_after_study = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="是否学完就业"
    )
    responsible_person = models.CharField(max_length=30, null=True, blank=True, verbose_name="负责人")

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = "客户信息"
        verbose_name_plural = "客户信息列表"


class StudyProgressHistory(models.Model):
    """
    学习进度历史记录模型
    """
    client = models.ForeignKey(
        ClientData,
        on_delete=models.CASCADE,
        related_name="study_progress_histories",
        verbose_name="客户"
    )
    progress_content = models.TextField(verbose_name="学习进度内容")
    modified_by = models.CharField(max_length=50, verbose_name="修改人")
    modified_at = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "学习进度历史记录"
        verbose_name_plural = "学习进度历史记录"

    def __str__(self):
        return f"{self.client.name} - 修改时间: {self.modified_at}"


class FollowUpRecordHistory(models.Model):
    """
    跟进记录历史记录模型
    """
    client = models.ForeignKey(
        ClientData,
        on_delete=models.CASCADE,
        related_name="follow_up_record_histories",
        verbose_name="客户"
    )
    record_content = models.TextField(verbose_name="跟进记录内容")
    modified_by = models.CharField(max_length=50, verbose_name="修改人")
    modified_at = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    record_audio = models.FileField(
        upload_to=follow_up_audio_upload_path,
        storage= get_audio_storage,  # 使用存储类的路径字符串
        verbose_name="通话录音",
        null=True,
        blank=True
    )
    record_image = models.ImageField(
        upload_to=follow_up_image_upload_path,
        storage= get_image_storage,  # 使用存储类的路径字符串
        verbose_name="聊天截图",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "跟进记录历史记录"
        verbose_name_plural = "跟进记录历史记录"

    def __str__(self):
        return f"{self.client.name} - 修改时间: {self.modified_at}"


class SituationAnalysisHistory(models.Model):
    """
    情况分析历史记录模型
    """
    client = models.ForeignKey(
        ClientData,
        on_delete=models.CASCADE,
        related_name="situation_analysis_histories",
        verbose_name="客户"
    )
    analysis_content = models.TextField(verbose_name="情况分析内容")
    modified_by = models.CharField(max_length=50, verbose_name="修改人")
    modified_at = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "情况分析历史记录"
        verbose_name_plural = "情况分析历史记录"

    def __str__(self):
        return f"{self.client.name} - 修改时间: {self.modified_at}"