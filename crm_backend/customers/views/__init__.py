# /home/myproject/crm_backend/customers/views/__init__.py

# 导入各个功能模块的视图函数
from .views_customer_list import customerlist,check_new_comments
from .views_daily_report import daily_report
from .views_customer_add import add_customer
from .views_customer_edit import edit_customer
from .views_analysis import data_analysis,analysis_data_json,product_manager_daily_report,get_completion_data
from .views_customer_detail import customer_detail
from .views_customer_delete import delete_customer
from .views_dashboard import dashboard

# 定义 __all__，统一管理导出的函数
__all__ = [
    "customerlist",
    "daily_report",
    "add_customer",
    "edit_customer",
    "data_analysis",
    "customer_detail",
    "delete_customer",
    "dashboard",
    "analysis_data_json",
    "product_manager_daily_report",
    "get_completion_data",
    "check_new_comments",
]