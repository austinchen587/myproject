import csv
from django.core.management.base import BaseCommand
from employee.models import Employee
from datetime import datetime
import os


class Command(BaseCommand):
    help = "Import employee data from a CSV file into the Employee model"

    def handle(self, *args, **kwargs):
        # CSV 文件路径
        csv_file_path = os.path.join(
            os.path.dirname(__file__), "employ.csv"
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
                    birth_date = self.parse_date(row.get("出生日期"))
                    entry_date = self.parse_date(row.get("入职时间"))
                    last_working_day = self.parse_date(row.get("最后工作日日期"))
                    contract_start_date = self.parse_date(row.get("开始日期"))
                    contract_end_date = self.parse_date(row.get("到期日期"))
                    age = self.parse_age(row.get("年龄"))
                    seniority_days = self.parse_int(row.get("工龄/天数"))

                    # 确保必填字段不为空
                    if not row.get("姓名"):
                        self.stdout.write(self.style.WARNING(f"Skipping row: 姓名为空"))
                        skipped_count += 1
                        continue
                    if not row.get("身份证号码"):
                        self.stdout.write(self.style.WARNING(f"Skipping row: {row.get('姓名', '未知')} - 身份证号码为空"))
                        skipped_count += 1
                        continue

                    # 创建 Employee 对象
                    Employee.objects.create(
                        serial_number=int(row.get("序号", 0)),
                        name=row.get("姓名", "未知")[:100],
                        department=row.get("部门", "未知")[:100],
                        position=row.get("岗位", "未知")[:100],
                        id_card_number=row.get("身份证号码", "未知")[:18],
                        gender=row.get("性别", "未知")[:10],
                        age=age,
                        birth_date=birth_date,
                        phone_number=str(row.get("联系电话", "")).strip()[:15] if row.get("联系电话") else None,
                        education=row.get("学历", "未知")[:50],
                        native_place=row.get("籍贯", "未知")[:100],
                        marital_status=row.get("婚姻状况", "未知")[:20],
                        entry_date=entry_date,
                        seniority_days=seniority_days,
                        current_address=row.get("现居地址", "未知")[:255],
                        labor_contract_type=row.get("劳动合同类型", "未知")[:100],
                        contract_start_date=contract_start_date,
                        contract_end_date=contract_end_date,
                        status=row.get("状态", "未知")[:20],
                        last_working_day=last_working_day,
                        resignation_reason=row.get("离职原因", None)[:255] if row.get("离职原因") else None,
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row: {row.get('姓名', '未知')} - {e}"))
                    skipped_count += 1

        # 输出成功导入的记录数量和跳过的记录数量
        self.stdout.write(self.style.SUCCESS(f"Data imported successfully. {count} records were added."))
        self.stdout.write(self.style.WARNING(f"{skipped_count} records were skipped due to errors."))

    def parse_date(self, date_str):
        """
        解析日期字段为 datetime 对象，格式为 'YYYY-MM-DD' 或 'YYYY年MM月DD日'，如果失败则返回 None
        """
        try:
            if "年" in date_str and "月" in date_str and "日" in date_str:
                return datetime.strptime(date_str, "%Y年%m月%d日").date()
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

    def parse_int(self, int_str):
        """
        解析整数字段，如果失败则返回 None
        """
        try:
            return int(float(int_str)) if int_str else None
        except (ValueError, TypeError):
            return None