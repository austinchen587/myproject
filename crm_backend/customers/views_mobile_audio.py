from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer, Recording
import os
import mimetypes
import time
import hashlib
import subprocess
from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)

def get_file_hash(file):
    """计算文件的哈希值"""
    hasher = hashlib.md5()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()

@login_required
def upload_audio(request, customer_id):
    logger.debug(f"Received request to upload audio for customer_id={customer_id}")
    if request.method == "POST":
        if "audio_file" not in request.FILES:
            logger.error("No audio file in request.")
            return JsonResponse({"error": "未接收到音频文件"}, status=400)

        audio_file = request.FILES["audio_file"]
        customer = get_object_or_404(Customer, id=customer_id)
        
        recording = Recording.objects.create(customer=customer, audio_file=audio_file)
        logger.info(f"Audio file {audio_file.name} uploaded successfully for customer {customer_id}")

        return JsonResponse({
            "message": "录音文件上传成功！",
            "file_url": recording.audio_file.url,
            "uploaded_at": recording.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "recording_id": recording.id
        })

    return JsonResponse({"error": "无效的请求方法"}, status=400)

@login_required
def delete_audio(request, recording_id):
    """
    删除客户录音
    """
    logger.debug(f"Received request to delete audio with recording_id={recording_id}")
    if request.method == "POST":
        try:
            # 获取要删除的记录
            recording = get_object_or_404(Recording, id=recording_id)

            # 删除录音文件及数据库记录
            if recording.audio_file:
                logger.info(f"Attempting to delete audio file: {recording.audio_file.name}")
                try:
                    recording.audio_file.delete()
                    logger.info(f"Audio file {recording.audio_file.name} deleted successfully")
                except Exception as e:
                    logger.error(f"Error deleting audio file {recording.audio_file.name}: {e}")
                    return JsonResponse({"error": "音频文件删除失败"}, status=500)

            # 删除数据库记录
            recording.delete()
            logger.info(f"Recording with id={recording_id} deleted successfully")
            return JsonResponse({"message": "音频文件删除成功！"})
        except Exception as e:
            logger.error(f"删除音频失败: {e}")
            return JsonResponse({"error": "音频删除失败"}, status=500)

    return JsonResponse({"error": "无效的请求方法"}, status=400)


@login_required
def customer_audio_view(request, customer_id):
    """
    返回与客户相关的音频数据。
    """
    customer = get_object_or_404(Customer, id=customer_id)
    recordings = Recording.objects.filter(customer=customer, audio_file__isnull=False).order_by('-created_at')

    return render(request, 'mobile/components/customer_mobile_audio.html', {
        'customer': customer,
        'recordings': recordings,
    })