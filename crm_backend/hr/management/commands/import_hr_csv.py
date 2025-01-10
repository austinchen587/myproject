import csv
from django.core.management.base import BaseCommand
from hr.models import Candidate
from datetime import datetime
import os


class Command(BaseCommand):
    help = "Import HR data from a cleaned CSV file into the Candidate model"

    def handle(self, *args, **kwargs):
        # CSV 文件路径
        csv_file_path = os.path.join(
            os.path.dirname(__file__), "cleaned_hr_inter.csv"
        )

        # 检查文件是否存在
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f"The file {csv_file_path} does not exist."))
            return

        # 读取 CSV 文件
        with open(csv_file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            count = 0  # 成功导入的记录数
            skipped_count = 0  # 跳过的记录数

            for row in reader:
                try:
                    # 解析字段
                    interview_date = self.parse_date(row.get("面试日期"))
                    employment_date = self.parse_date(row.get("入职日期"))
                    age = self.parse_age(row.get("年龄"))
                    passed_3_day_trial = self.parse_boolean(row.get("是否通过\n3天试岗"))
                    is_employed = self.parse_boolean(row.get("是否入职"))

                    # 确保必填字段不为空
                    if not interview_date:
                        self.stdout.write(self.style.WARNING(f"Skipping row: {row.get('求职者', '未知')} - 面试日期为空"))
                        skipped_count += 1
                        continue
                    if not row.get("求职者"):
                        self.stdout.write(self.style.WARNING(f"Skipping row: 面试日期: {interview_date} - 求职者姓名为空"))
                        skipped_count += 1
                        continue

                    # 创建 Candidate 对象
                    Candidate.objects.create(
                        interview_date=interview_date,
                        candidate_name=row.get("求职者", "未知")[:100],  # 限制最大长度为 100
                        job_position=row.get("求职岗位", "未知")[:100],  # 限制最大长度为 100
                        gender=row.get("性别", "未知")[:10],  # 限制最大长度为 10
                        phone_number=row.get("手机号码", None)[:20] if row.get("手机号码") else None,  # 手机号可为空
                        age=age,
                        marital_status=row.get("婚姻状况", None)[:50] if row.get("婚姻状况") else None,
                        has_sales_experience=self.parse_boolean(row.get("是否做过销售")),
                        initial_interviewer=row.get("初试官", None)[:100] if row.get("初试官") else None,
                        final_interviewer=row.get("复试官", None)[:100] if row.get("复试官") else None,
                        interview_result=row.get("面试结果", "未知")[:100],
                        rejection_reason=row.get("不通过原因", None)[:200] if row.get("不通过原因") else None,
                        inviter=row.get("邀约人", None)[:100] if row.get("邀约人") else None,
                        invitation_channel=row.get("邀约渠道", None)[:100] if row.get("邀约渠道") else None,
                        is_employed=is_employed,
                        employment_date=employment_date,
                        passed_3_day_trial=passed_3_day_trial,
                        tracking_1_month=row.get("入职1个月跟踪", None)[:200] if row.get("入职1个月跟踪") else None,
                        tracking_3_months=row.get("入职3个月跟踪", None)[:200] if row.get("入职3个月跟踪") else None,
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row: {row.get('求职者', '未知')} - {e}"))
                    skipped_count += 1

        # 输出成功导入的记录数量和跳过的记录数量
        self.stdout.write(self.style.SUCCESS(f"Data imported successfully. {count} records were added."))
        self.stdout.write(self.style.WARNING(f"{skipped_count} records were skipped due to errors."))

    def parse_date(self, date_str):
        """
        解析日期字段为 datetime 对象，格式为 'YYYY年MM月DD日' 转换为 'YYYY-MM-DD'，如果失败则返回 None
        """
        try:
            return datetime.strptime(date_str, "%Y年%m月%d日").date() if date_str else None
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

    def parse_boolean(self, bool_str):
        """
        解析布尔字段，将 '是' 转换为 True，'否' 转换为 False，其它值返回 None
        """
        if bool_str == "是":
            return True
        elif bool_str == "否":
            return False
        return None