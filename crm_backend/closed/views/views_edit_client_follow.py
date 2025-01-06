from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction
from ..models import ClientData, StudyProgressHistory, FollowUpRecordHistory, SituationAnalysisHistory
from decimal import Decimal, InvalidOperation
import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

@transaction.atomic
def update_client_follow(request, client_id):
    client = get_object_or_404(ClientData, id=client_id)

    if request.method == "POST":
        try:
            updated_by = request.user.username
            logger.debug(f"用户 {updated_by} 正在更新客户 {client_id} 信息")

            # 初始化是否有更改的标志
            has_changes = False

            # 更新学习进度
            new_study_progress = request.POST.get("study_progress", "").strip()
            if new_study_progress and new_study_progress != client.study_progress:
                StudyProgressHistory.objects.create(
                    client=client,
                    progress_content=new_study_progress,
                    modified_by=updated_by,
                )
                client.study_progress = new_study_progress
                logger.debug(f"学习进度更新为: {new_study_progress}")
                has_changes = True

            # 更新跟进记录
            new_follow_up_record = request.POST.get("follow_up_record", "").strip()
            record_audios = request.FILES.getlist("record_audio")  # 获取多个语音文件
            record_images = request.FILES.getlist("record_image")  # 获取多个图片文件

            if new_follow_up_record or record_audios or record_images:
                for record_audio in record_audios:
                    validate_file(record_audio, max_size=100 * 1024 * 1024, allowed_types=["audio/mpeg", "audio/wav"], file_type="语音文件")
                    logger.debug(f"语音文件接收成功: {record_audio.name}, 大小: {record_audio.size}")
                    FollowUpRecordHistory.objects.create(
                        client=client,
                        record_content=new_follow_up_record or client.follow_up_record,
                        modified_by=updated_by,
                        record_audio=record_audio,
                    )
                    has_changes = True

                for record_image in record_images:
                    validate_file(record_image, max_size=50 * 1024 * 1024, allowed_types=["image/jpeg", "image/png"], file_type="图片文件")
                    logger.debug(f"图片文件接收成功: {record_image.name}, 大小: {record_image.size}")
                    FollowUpRecordHistory.objects.create(
                        client=client,
                        record_content=new_follow_up_record or client.follow_up_record,
                        modified_by=updated_by,
                        record_image=record_image,
                    )
                    has_changes = True

                if new_follow_up_record:
                    client.follow_up_record = new_follow_up_record
                    logger.debug(f"跟进记录更新为: {new_follow_up_record}")
                    has_changes = True

            # 更新情况分析
            new_situation_analysis = request.POST.get("situation_analysis", "").strip()
            if new_situation_analysis and new_situation_analysis != client.situation_analysis:
                SituationAnalysisHistory.objects.create(
                    client=client,
                    analysis_content=new_situation_analysis,
                    modified_by=updated_by,
                )
                client.situation_analysis = new_situation_analysis
                logger.debug("情况分析历史已创建")
                has_changes = True

            # 更新其他字段
            has_other_changes = update_client_fields(request, client)
            has_changes = has_changes or has_other_changes

            if has_changes:
                client.save()
                logger.debug(f"客户 {client_id} 更新成功")
                return redirect(reverse("closed:client_data_list_follow"))
            else:
                logger.debug(f"客户 {client_id} 没有任何修改")
                return render(request, "closed/closed_update_follow.html", {"client": client})

        except ValidationError as ve:
            logger.error(f"验证失败: {ve}")
            return render(request, "closed/closed_update_follow.html", {"client": client, "error": str(ve)})
        except Exception as e:
            logger.error(f"未知错误: {e}, 客户 ID: {client_id}", exc_info=True)
            return render(request, "closed/closed_update_follow.html", {"client": client, "error": "系统错误，请稍后再试"})

    return render(request, "closed/closed_update_follow.html", {"client": client})


def validate_file(file, max_size, allowed_types, file_type):
    """
    验证上传文件的大小和类型。
    """
    if file.size > max_size:
        raise ValidationError(f"{file_type}大小不能超过 {max_size // (1024 * 1024)}MB")
    if file.content_type not in allowed_types:
        raise ValidationError(f"{file_type}类型不支持，仅支持: {', '.join(allowed_types)}")


def update_client_fields(request, client):
    """
    更新客户的基础字段。返回是否有修改的标志。
    """
    has_changes = False
    fields_to_update = [
        "registration_date", "source_channel", "name", "gender", "age",
        "education", "major", "employment_status", "phone", "sales_teacher",
        "problem_exists", "solution", "remarks", "deal_status", "payment_method",
        "payment_amount", "customer_summary"
    ]

    for field in fields_to_update:
        new_value = request.POST.get(field)
        if new_value and getattr(client, field) != new_value:
            if field == "payment_amount":
                try:
                    new_value = Decimal(new_value)
                except InvalidOperation:
                    logger.error(f"支付金额 {new_value} 无效")
                    new_value = None
            setattr(client, field, new_value)
            has_changes = True
            logger.debug(f"{field} 更新为: {new_value}")

    return has_changes