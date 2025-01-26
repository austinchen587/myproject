from django.db import models
from hr.storages.aliyun_storages import AliyunOSSHRStorage


def get_aliyun_storage():
    """返回 Aliyun OSS HR 存储实例"""
    return AliyunOSSHRStorage()


class Candidate(models.Model):
    # 字段定义
    interview_date = models.DateField(verbose_name="面试日期")  # 面试日期
    candidate_name = models.CharField(max_length=100, verbose_name="求职者")  # 求职者
    job_position = models.CharField(max_length=100, verbose_name="求职岗位")  # 求职岗位
    gender = models.CharField(max_length=10, verbose_name="性别")  # 性别
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="手机号码")  # 手机号码
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="年龄")  # 年龄
    marital_status = models.CharField(max_length=50, null=True, blank=True, verbose_name="婚姻状况")  # 婚姻状况
    has_sales_experience = models.BooleanField(null=True, blank=True, verbose_name="是否做过销售")  # 是否做过销售
    initial_interviewer = models.CharField(max_length=100, null=True, blank=True, verbose_name="初试官")  # 初试官
    final_interviewer = models.CharField(max_length=100, null=True, blank=True, verbose_name="复试官")  # 复试官
    interview_result = models.CharField(max_length=100, verbose_name="面试结果")  # 面试结果
    rejection_reason = models.CharField(max_length=200, null=True, blank=True, verbose_name="不通过原因")  # 不通过原因
    inviter = models.CharField(max_length=100, null=True, blank=True, verbose_name="邀约人")  # 邀约人
    invitation_channel = models.CharField(max_length=100, null=True, blank=True, verbose_name="邀约渠道")  # 邀约渠道
    is_employed = models.BooleanField(null=True, blank=True, verbose_name="是否入职")  # 是否入职
    employment_date = models.DateField(null=True, blank=True, verbose_name="入职日期")  # 入职日期
    passed_3_day_trial = models.BooleanField(null=True, blank=True, verbose_name="是否通过3天试岗")  # 是否通过3天试岗
    tracking_1_month = models.CharField(max_length=200, null=True, blank=True, verbose_name="入职1个月跟踪")  # 入职1个月跟踪
    tracking_3_months = models.CharField(max_length=200, null=True, blank=True, verbose_name="入职3个月跟踪")  # 入职3个月跟踪

    photo = models.ImageField(
        storage= get_aliyun_storage(),
        upload_to="candidates/photos/", 
        null=True, 
        blank=True, 
        verbose_name="面试照片"
    )  # 面试照片


    class Meta:
        verbose_name = "候选人"
        verbose_name_plural = "候选人"

    def __str__(self):
        return f"{self.candidate_name} - {self.job_position}"