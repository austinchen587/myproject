from django.core.management.base import BaseCommand
from customers.models import Customer, DescriptionHistory
from sales.models import SalesUser
from django.utils.timezone import now


class Command(BaseCommand):
    help = "将 Customer 表中现有的 description 数据迁移到 DescriptionHistory 表，避免重复迁移"

    def handle(self, *args, **options):
        # 获取需要迁移的客户（description 非空且未迁移过）
        customers = Customer.objects.filter(
            description__isnull=False
        ).exclude(description="").exclude(
            description_history__isnull=False  # 排除已有历史记录的客户
        )

        if not customers.exists():
            self.stdout.write(self.style.WARNING("没有需要迁移的客户描述数据"))
            return

        for customer in customers:
            # 确定更新人（默认设置为空或系统管理员）
            updated_by = customer.updated_by if customer.updated_by else None

            # 创建描述历史记录
            DescriptionHistory.objects.create(
                customer=customer,
                old_description="",  # 初始记录无旧描述
                new_description=customer.description,
                modified_by=updated_by,
                modified_at=customer.updated_at if customer.updated_at else now(),
            )

        self.stdout.write(self.style.SUCCESS(f"成功将 {customers.count()} 条描述迁移到 DescriptionHistory 表"))