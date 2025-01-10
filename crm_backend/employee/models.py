from django.db import models

class Employee(models.Model):
    # 字段定义
    name = models.CharField(max_length=100, verbose_name="姓名")  # 姓名
    department = models.CharField(max_length=100, verbose_name="部门")  # 部门
    position = models.CharField(max_length=100, verbose_name="岗位")  # 岗位
    id_card_number = models.CharField(max_length=18, unique=True, verbose_name="身份证号码")  # 身份证号码
    gender = models.CharField(max_length=10, choices=[("男", "男"), ("女", "女")], verbose_name="性别")  # 性别
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="年龄")  # 年龄
    birth_date = models.DateField(null=True, blank=True, verbose_name="出生日期")  # 出生日期
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="联系电话")  # 联系电话
    education = models.CharField(max_length=50, null=True, blank=True, verbose_name="学历")  # 学历
    native_place = models.CharField(max_length=100, null=True, blank=True, verbose_name="籍贯")  # 籍贯
    marital_status = models.CharField(max_length=20, null=True, blank=True, verbose_name="婚姻状况")  # 婚姻状况
    entry_date = models.DateField(null=True, blank=True, verbose_name="入职时间")  # 入职时间
    seniority_days = models.PositiveIntegerField(null=True, blank=True, verbose_name="工龄/天数")  # 工龄/天数
    current_address = models.CharField(max_length=255, null=True, blank=True, verbose_name="现居地址")  # 现居地址
    labor_contract_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="劳动合同类型")  # 劳动合同类型
    contract_start_date = models.DateField(null=True, blank=True, verbose_name="开始日期")  # 合同开始日期
    contract_end_date = models.DateField(null=True, blank=True, verbose_name="到期日期")  # 合同到期日期
    status = models.CharField(max_length=20, choices=[("在职", "在职"), ("离职", "离职")], verbose_name="状态")  # 状态
    last_working_day = models.DateField(null=True, blank=True, verbose_name="最后工作日日期")  # 最后工作日日期
    resignation_reason = models.CharField(max_length=255, null=True, blank=True, verbose_name="离职原因")  # 离职原因

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = "员工信息"
        ordering = ["entry_date"]  # 按入职时间排序

    def __str__(self):
        return f"{self.name} - {self.position}"