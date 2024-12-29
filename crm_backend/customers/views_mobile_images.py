from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Customer, Recording
import logging
from django.conf import settings

logger = logging.getLogger(__name__)
logger.debug(f"OSS_IMAGES_BUCKET_NAME: {settings.OSS_IMAGES_BUCKET_NAME}")


@login_required
def upload_image(request, customer_id):
    logger.debug(f"Received request to upload image for customer_id={customer_id}")
    if request.method == "POST":
        if "image_files" not in request.FILES:
            logger.error("No image files in request.")
            return JsonResponse({"error": "未接收到图片文件"}, status=400)

        customer = get_object_or_404(Customer, id=customer_id)
        image_files = request.FILES.getlist("image_files")  # 获取多个文件

        uploaded_files = []
        for image_file in image_files:
            # 检查文件类型和大小
            if not image_file.content_type.startswith("image/"):
                logger.error(f"File {image_file.name} is not an image.")
                continue
            if image_file.size > 5 * 1024 * 1024:  # 限制图片大小为 5MB
                logger.error(f"File {image_file.name} exceeds size limit.")
                continue

            try:
                # 存储文件
                recording = Recording.objects.create(customer=customer, image_file=image_file)
                logger.debug(f"Created Recording ID: {recording.id}, Image File: {recording.image_file}")
                uploaded_files.append({
                    "file_url": recording.image_file.url,
                    "uploaded_at": recording.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    "recording_id": recording.id,
                })
            except Exception as e:
                logger.error(f"图片上传失败: {e}")

        if uploaded_files:
            return JsonResponse({
                "message": "部分或全部图片上传成功！",
                "uploaded_files": uploaded_files,
            })
        else:
            return JsonResponse({"error": "图片上传失败"}, status=500)

    return JsonResponse({"error": "无效的请求方法"}, status=400)


@login_required
def delete_image(request, recording_id):
    """
    删除客户图片
    """
    logger.debug(f"Received request to delete image with recording_id={recording_id}")
    if request.method == "POST":
        try:
            # 获取要删除的记录
            recording = get_object_or_404(Recording, id=recording_id)

            # 删除图片文件及数据库记录
            if recording.image_file:
                logger.info(f"Attempting to delete file: {recording.image_file.name}")
                try:
                    recording.image_file.delete()
                    logger.info(f"File {recording.image_file.name} deleted successfully")
                except Exception as e:
                    logger.error(f"Error deleting file {recording.image_file.name}: {e}")
                    return JsonResponse({"error": "图片文件删除失败"}, status=500)

            # 删除数据库记录
            recording.delete()
            logger.info(f"Recording with id={recording_id} deleted successfully")
            return JsonResponse({"message": "图片文件删除成功！"})
        except Exception as e:
            logger.error(f"删除图片失败: {e}")
            return JsonResponse({"error": "图片删除失败"}, status=500)

    return JsonResponse({"error": "无效的请求方法"}, status=400)


@login_required
def customer_images_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    recordings = Recording.objects.filter(customer=customer, image_file__isnull=False).order_by('-created_at')

    logger.debug(f"Customer ID: {customer.id}")
    logger.debug(f"Recordings Count (QuerySet): {recordings.count()}")
    for rec in recordings:
        if rec.image_file:  # 确保 image_file 存在
            logger.debug(f"Recording ID: {rec.id}, URL: {rec.image_file.url}")
        else:
            logger.debug(f"Recording ID: {rec.id} has no associated image file.")

    return render(request, 'test_customer_images.html', {
        'customer': customer,
        'recordings': recordings,
    })


@login_required
def test_customer_images_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    recordings = Recording.objects.filter(customer=customer, image_file__isnull=False).order_by('-created_at')

    logger.debug(f"Customer ID: {customer.id}")
    logger.debug(f"Recordings Count (QuerySet): {recordings.count()}")
    for rec in recordings:
        if rec.image_file:
            logger.debug(f"Recording ID: {rec.id}, URL: {rec.image_file.url}")
        else:
            logger.debug(f"Recording ID: {rec.id} has no associated image file.")

    return render(request, 'test_customer_images.html', {
        'customer': customer,
        'recordings': recordings,
    })