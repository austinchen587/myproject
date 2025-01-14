from django.shortcuts import render
from django.db.models import Count, Q
from ..models import Candidate
import pandas as pd
from datetime import date

def hr_analysis_view(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)

    # 默认时间范围：当前月第一天到今天
    today = date.today()
    if not start_date:
        start_date = today.replace(day=1).isoformat()
    if not end_date:
        end_date = today.isoformat()

    # 数据查询，按时间范围筛选
    queryset = Candidate.objects.filter(
        interview_date__range=[start_date, end_date]
    )

    # 第一个报表：按初试官统计面试量和通过量
    initial_interviewer_data = queryset.values("initial_interviewer").annotate(
        total_interviews=Count("id"),
        passed_interviews=Count("id", filter=Q(interview_result="通过")),
    ).order_by("-total_interviews")

    # 转换为 DataFrame
    if initial_interviewer_data.exists():
        df_initial = pd.DataFrame.from_records(initial_interviewer_data)
        df_initial.rename(columns={
            "initial_interviewer": "初试官",
            "total_interviews": "面试总量",
            "passed_interviews": "通过量",
        }, inplace=True)
        # 添加汇总行
        summary_initial = pd.DataFrame({
            "初试官": ["汇总"],
            "面试总量": [df_initial["面试总量"].sum()],
            "通过量": [df_initial["通过量"].sum()],
        })
        df_initial = pd.concat([df_initial, summary_initial], ignore_index=True)
    else:
        df_initial = pd.DataFrame(columns=["初试官", "面试总量", "通过量"])

    # 第二个报表：按邀约人统计邀约渠道
    inviter_data = queryset.values("inviter", "invitation_channel").annotate(
        total_invites=Count("id")
    ).order_by("inviter")

    if inviter_data.exists():
        df_inviter = pd.DataFrame.from_records(inviter_data)
        df_inviter.rename(columns={
            "inviter": "邀约人",
            "invitation_channel": "邀约渠道",
            "total_invites": "邀约总量",
        }, inplace=True)
        # 添加汇总行
        summary_inviter = pd.DataFrame({
            "邀约人": ["汇总"],
            "邀约渠道": [""],  # 汇总行渠道为空
            "邀约总量": [df_inviter["邀约总量"].sum()],
        })
        df_inviter = pd.concat([df_inviter, summary_inviter], ignore_index=True)
    else:
        df_inviter = pd.DataFrame(columns=["邀约人", "邀约渠道", "邀约总量"])

    # 数据传递到模板
    context = {
        "start_date": start_date,
        "end_date": end_date,
        "df_initial": df_initial.to_html(index=False, classes="table table-striped"),
        "df_inviter": df_inviter.to_html(index=False, classes="table table-striped"),
    }
    return render(request, "hr/hr_analysis.html", context)