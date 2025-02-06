from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction
from urllib.parse import urlencode
from ..models import ClientData, StudyProgressHistory, FollowUpRecordHistory, SituationAnalysisHistory
from decimal import Decimal, InvalidOperation
import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

@transaction.atomic
def update_client_follow(request, client_id):
    client = get_object_or_404(ClientData, id=client_id)

    # **获取筛选条件和当前页码**
    query_params = request.GET.copy()
    page_number = query_params.get("page", "1")  # 默认 1，防止 None
    query_params.pop("page", None)  # **先删除所有 `page`，避免重复**
    
    query_string = query_params.urlencode()  # 重新编码查询参数

    if request.method == "POST":
        try:
            updated_by = request.user.username
            logger.debug(f"用户 {updated_by} 正在更新客户 {client_id} 信息")

            has_changes = False

            # **更新学习进度**
            new_study_progress = request.POST.get("study_progress", "").strip()
            if new_study_progress and new_study_progress != client.study_progress:
                StudyProgressHistory.objects.create(
                    client=client,
                    progress_content=new_study_progress,
                    modified_by=updated_by,
                )
                client.study_progress = new_study_progress
                has_changes = True

            # **更新跟进记录**
            new_follow_up_record = request.POST.get("follow_up_record", "").strip()
            record_audios = request.FILES.getlist("record_audio")
            record_images = request.FILES.getlist("record_image")

            if new_follow_up_record or record_audios or record_images:
                for record_audio in record_audios:
                    validate_file(record_audio, max_size=100 * 1024 * 1024, allowed_types=["audio/mpeg", "audio/wav"])
                    FollowUpRecordHistory.objects.create(
                        client=client,
                        record_content=new_follow_up_record or client.follow_up_record,
                        modified_by=updated_by,
                        record_audio=record_audio,
                    )
                    has_changes = True

                for record_image in record_images:
                    validate_file(record_image, max_size=50 * 1024 * 1024, allowed_types=["image/jpeg", "image/png"])
                    FollowUpRecordHistory.objects.create(
                        client=client,
                        record_content=new_follow_up_record or client.follow_up_record,
                        modified_by=updated_by,
                        record_image=record_image,
                    )
                    has_changes = True

                if new_follow_up_record:
                    client.follow_up_record = new_follow_up_record
                    has_changes = True

            # **更新情况分析**
            new_situation_analysis = request.POST.get("situation_analysis", "").strip()
            if new_situation_analysis and new_situation_analysis != client.situation_analysis:
                SituationAnalysisHistory.objects.create(
                    client=client,
                    analysis_content=new_situation_analysis,
                    modified_by=updated_by,
                )
                client.situation_analysis = new_situation_analysis
                has_changes = True

            # **更新其他字段**
            has_other_changes = update_client_fields(request, client)
            has_changes = has_changes or has_other_changes

            if has_changes:
                client.save()
                logger.debug(f"客户 {client_id} 更新成功")

                # **🔹 重新生成 URL，确保 `page` 只出现一次**
                redirect_url = f"{reverse('closed:client_data_list_follow')}?page={page_number}&{query_string}"
                return redirect(redirect_url)

            else:
                logger.debug(f"客户 {client_id} 没有任何修改")
                return render(request, "closed/closed_update_follow.html", {
                    "client": client,
                    "query_string": query_string,
                    "page": page_number,
                })

        except ValidationError as ve:
            logger.error(f"验证失败: {ve}")
            return render(request, "closed/closed_update_follow.html", {"client": client, "error": str(ve)})
        except Exception as e:
            logger.error(f"未知错误: {e}, 客户 ID: {client_id}", exc_info=True)
            return render(request, "closed/closed_update_follow.html", {"client": client, "error": "系统错误，请稍后再试"})

    return render(request, "closed/closed_update_follow.html", {
        "client": client,
        "query_string": query_string,
        "page": page_number,
    })


def validate_file(file, max_size, allowed_types):
    """验证上传文件的大小和类型"""
    if file.size > max_size:
        raise ValidationError(f"文件大小不能超过 {max_size // (1024 * 1024)}MB")
    if file.content_type not in allowed_types:
        raise ValidationError(f"文件类型不支持，仅支持: {', '.join(allowed_types)}")


def update_client_fields(request, client):
    """更新客户的基础字段，并返回是否有修改"""
    has_changes = False
    fields_to_update = [
        "registration_date", "source_channel", "name", "gender", "age",
        "education", "major", "employment_status", "phone", "sales_teacher",
        "problem_exists", "solution", "remarks", "deal_status", "payment_method",
        "payment_amount", "customer_summary",
    ]

    for field in fields_to_update:
        new_value = request.POST.get(field)
        if new_value and getattr(client, field) != new_value:
            if field == "payment_amount":
                try:
                    new_value = Decimal(new_value)
                except InvalidOperation:
                    new_value = None
            setattr(client, field, new_value)
            has_changes = True

    # **更新 `is_on_leave`（是否请假）**
    is_on_leave_value = request.POST.get("is_on_leave", "off")
    new_is_on_leave = is_on_leave_value == "on"  # "on" 表示 True，否则 False
    if new_is_on_leave != client.is_on_leave:
        client.is_on_leave = new_is_on_leave
        has_changes = True

    return has_changes