from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    # 列表显示的字段
    list_display = (
        "candidate_name",
        "job_position",
        "gender",
        "phone_number",
        "age",
        "marital_status",
        "has_sales_experience",
        "initial_interviewer",
        "final_interviewer",
        "interview_result",
        "is_employed",
        "employment_date",
        "passed_3_day_trial",
    )

    # 可搜索的字段
    search_fields = ("candidate_name", "job_position", "phone_number", "initial_interviewer", "final_interviewer")

    # 过滤器
    list_filter = (
        "gender",
        "interview_result",
        "is_employed",
        "has_sales_experience",
        "passed_3_day_trial",
        "employment_date",
    )

    # 可编辑的字段（直接在列表页面编辑）
    list_editable = ("interview_result", "is_employed", "employment_date", "passed_3_day_trial")

    # 日期层级导航
    date_hierarchy = "employment_date"

    # 字段分组显示
    fieldsets = (
        ("基本信息", {
            "fields": ("candidate_name", "job_position", "gender", "phone_number", "age", "marital_status"),
        }),
        ("面试信息", {
            "fields": ("interview_date", "has_sales_experience", "initial_interviewer", "final_interviewer", "interview_result", "rejection_reason"),
        }),
        ("邀约信息", {
            "fields": ("inviter", "invitation_channel"),
        }),
        ("入职信息", {
            "fields": ("is_employed", "employment_date", "passed_3_day_trial", "tracking_1_month", "tracking_3_months"),
        }),
    )

    # 默认排序
    ordering = ("-employment_date",)

    # 每页显示的记录数
    list_per_page = 20