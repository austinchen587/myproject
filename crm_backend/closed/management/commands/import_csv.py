import csv
from django.core.management.base import BaseCommand
from closed.models import ClientData
from datetime import datetime
from decimal import Decimal, InvalidOperation
import os


class Command(BaseCommand):
    help = "Import data from a cleaned CSV file into the database"

    def handle(self, *args, **kwargs):
        # CSV 文件路径
        csv_file_path = "/app/crm_backend/closed/management/commands/cleaned_x.csv"

        # 检查文件是否存在
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f"The file {csv_file_path} does not exist."))
            return

        # 读取 CSV 文件
        with open(csv_file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            count = 0  # 记录成功导入的记录数

            for row in reader:
                try:
                    # 解析字段
                    registration_date = self.parse_date(row.get("日期"))
                    age = self.parse_age(row.get("年龄"))
                    payment_amount = self.parse_decimal(row.get("支付金额"))

                    # 创建 ClientData 对象
                    ClientData.objects.create(
                        registration_date=registration_date,
                        source_channel=row.get("来源渠道", "未知")[:150],  # 限制最大长度为 150
                        name=row.get("姓名", "未知")[:50],  # 限制最大长度为 50
                        gender=row.get("性别", "未知")[:30],  # 限制最大长度为 30
                        age=age,
                        education=row.get("学历", "未知")[:50],  # 限制最大长度为 50
                        major=row.get("专业", "未知")[:50],  # 限制最大长度为 50
                        employment_status=row.get("就业情况", "未知")[:150],  # 限制最大长度为 150
                        phone=row.get("电话", "未知")[:20],  # 限制最大长度为 20
                        sales_teacher=row.get("就业老师", "未知")[:50],  # 限制最大长度为 50
                        follow_up_record=row.get("跟进记录", "无记录"),
                        problem_exists=row.get("存在问题", "无问题"),
                        solution=row.get("解决办法", "无解决方案"),
                        remarks=row.get("备注", "无备注"),
                        deal_status=row.get("成交情况", "未知")[:150],  # 限制最大长度为 150
                        payment_method=row.get("支付方式", "未知")[:100],  # 限制最大长度为 100
                        payment_amount=payment_amount,
                        customer_summary=row.get("客户总结", "无总结"),
                        study_progress=row.get("学习进度", "无学习进度"),
                        problem_tracking=row.get("问题追踪", "无问题追踪"),
                        situation_analysis=row.get("情况分析", "无情况分析"),
                        is_employed_after_study=row.get("是否学完就业", "未知")[:100],  # 限制最大长度为 100
                        responsible_person=row.get("负责人", "未知")[:30],  # 限制最大长度为 30
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row: {e}"))

        # 输出成功导入的记录数量
        self.stdout.write(self.style.SUCCESS(f"Data imported successfully. {count} records were added."))

    def parse_date(self, date_str):
        """
        解析日期字段为 datetime 对象，格式为 'YYYY-MM-DD'，如果失败则返回 None
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
        except (ValueError, TypeError):
            return None

    def parse_age(self, age_str):
        """
        解析年龄字段为整数，如果失败则返回 None
        """
        try:
            return int(float(age_str)) if age_str else None
        except (ValueError, TypeError):
            return None

    def parse_decimal(self, decimal_str):
        """
        解析支付金额字段为 Decimal 类型，如果失败则返回 Decimal('0.00')
        """
        try:
            return Decimal(decimal_str) if decimal_str else Decimal("0.00")
        except (InvalidOperation, TypeError):
            return Decimal("0.00")