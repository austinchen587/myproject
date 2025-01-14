from django.shortcuts import render
from django.db.models import Sum, Count
from closed.models import ClientData
import pandas as pd
from datetime import date

def sales_analysis_view(request):
    # 获取筛选参数
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)
    include_teachers = request.GET.getlist("include_teachers", None)  # 销售老师包含筛选
    exclude_teachers = request.GET.getlist("exclude_teachers", None)  # 销售老师排除筛选

    # 如果没有选择时间范围，默认设置为当前月的第一天到今天
    today = date.today()
    if not start_date:
        start_date = today.replace(day=1).isoformat()  # 当前月第一天
    if not end_date:
        end_date = today.isoformat()  # 今天

    # 获取所有销售老师的列表
    sales_teachers = ClientData.objects.values_list("sales_teacher", flat=True).distinct()

    # 数据查询，按日期范围筛选
    queryset = ClientData.objects.filter(
        registration_date__range=[start_date, end_date]
    )

    # 包含或排除销售老师的逻辑
    if include_teachers:
        queryset = queryset.filter(sales_teacher__in=include_teachers)
    if exclude_teachers:
        queryset = queryset.exclude(sales_teacher__in=exclude_teachers)

    # 按销售老师汇总统计
    grouped_data = queryset.values("sales_teacher").annotate(
        total_amount=Sum("payment_amount"),
        total_count=Count("id"),
    ).order_by("-total_amount")  # 按销售金额从高到低排序

    # 转换为 DataFrame
    if grouped_data.exists():
        df = pd.DataFrame.from_records(grouped_data)
        # 替换列名为中文
        df.rename(columns={
            "sales_teacher": "销售老师",
            "total_amount": "总金额 (元)",
            "total_count": "总单量"
        }, inplace=True)
    else:
        df = pd.DataFrame(columns=["销售老师", "总金额 (元)", "总单量"])

    # 添加汇总行
    if not df.empty:
        summary_row = pd.DataFrame({
            "销售老师": ["汇总"],
            "总金额 (元)": [df["总金额 (元)"].sum()],
            "总单量": [df["总单量"].sum()],
        })
        df = pd.concat([df, summary_row], ignore_index=True)

    # 数据传递到模板
    context = {
        "sales_teachers": sales_teachers,
        "start_date": start_date,
        "end_date": end_date,
        "df": df.to_html(index=False, classes="table table-striped"),
        "selected_includes": include_teachers,
        "selected_excludes": exclude_teachers,
    }
    return render(request, "closed/closed_sales_analysis.html", context)