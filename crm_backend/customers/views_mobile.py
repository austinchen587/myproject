from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from .models import Customer, Recording,Comment
import mimetypes
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
import json
from sales.models import SalesUser
from django.utils.timezone import make_aware
from datetime import datetime, timedelta


@login_required
def mobile_view(request):
    today = datetime.today().date()
    default_start_date = today - timedelta(days=2)  # 默认显示最近2天

    # 获取筛选条件并提供默认值
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    phone_filter = request.GET.get('phone', '').strip()
    data_source_filter = request.GET.get('data_source', '').strip()
    student_batch_filter = request.GET.get('student_batch', '').strip()
    is_joined_filter = request.GET.get('is_joined', '').strip()
    created_by_filter = request.GET.get('created_by', '').strip()
    intention_filter = request.GET.get('intention', '').strip()

    # 日期处理
    try:
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        else:
            start_date = default_start_date  # 使用默认值

        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            end_date = today  # 使用默认值
    except ValueError:
        return JsonResponse({"error": "日期格式错误，请检查输入"}, status=400)

    # 转换为时区感知的 datetime
    start_datetime = make_aware(datetime.combine(start_date, datetime.min.time()))
    end_datetime = make_aware(datetime.combine(end_date, datetime.max.time()))

    # 初步筛选客户
    customers = Customer.objects.filter(created_at__range=(start_datetime, end_datetime))

    # 应用其他筛选条件
    if phone_filter:
        customers = customers.filter(phone__icontains=phone_filter)
    if data_source_filter:
        customers = customers.filter(data_source=data_source_filter)
    if student_batch_filter:
        if student_batch_filter.isdigit():
            customers = customers.filter(student_batch=int(student_batch_filter))
    if is_joined_filter in ['yes', 'no']:
        customers = customers.filter(is_joined=(is_joined_filter == 'yes'))
    if created_by_filter:
        if created_by_filter.isdigit():
            customers = customers.filter(created_by__id=int(created_by_filter))
    if intention_filter:
        customers = customers.filter(intention=intention_filter)

    # 按创建时间降序排列
    customers = customers.order_by('-created_at')

    # 获取所有 SalesUser 信息供筛选使用
    all_users = SalesUser.objects.all()

    # 渲染模板，传递筛选上下文
    return render(request, 'mobile/mobile_sub/customer_list.html', {
        "customers": customers,
        "user": request.user,
        "all_users": all_users,
        "start_date": start_date,
        "end_date": end_date,
        "phone_filter": phone_filter,
        "data_source_filter": data_source_filter,
        "student_batch_filter": student_batch_filter,
        "is_joined_filter": is_joined_filter,
        "created_by_filter": created_by_filter,
        "intention_filter": intention_filter,
    })

@login_required
def upload_audio(request, customer_id):
    """
    处理客户音频文件上传
    """
    if request.method == "POST":
        if "audio" not in request.FILES:
            return JsonResponse({"error": "未接收到音频文件"}, status=400)

        audio_file = request.FILES["audio"]
        file_extension = os.path.splitext(audio_file.name)[1].lower()
        allowed_extensions = [".wav", ".mp3", ".m4a", ".ogg", ".flac"]

        if file_extension not in allowed_extensions:
            return JsonResponse({"error": f"不支持的文件扩展名: {file_extension}"}, status=400)

        mime_type, _ = mimetypes.guess_type(audio_file.name)
        allowed_types = ["audio/wav", "audio/mpeg", "audio/x-m4a", "audio/ogg", "audio/flac"]
        if not mime_type or mime_type not in allowed_types:
            return JsonResponse({"error": f"不支持的文件类型: {mime_type}"}, status=400)

        customer = get_object_or_404(Customer, id=customer_id)
        customer.audio_file.save(audio_file.name, audio_file, save=True)

        return JsonResponse({"message": "音频文件上传成功！", "file_url": customer.audio_file.url})

    return JsonResponse({"error": "无效的请求"}, status=400)


@login_required
def customer_detail_mobile(request, id):
    customer = get_object_or_404(Customer, id=id)

    # 权限检查
    if request.user.role == 'user' and customer.created_by != request.user:
        messages.error(request, '您没有权限查看此客户')
        return redirect('customerlist')
    elif request.user.role == 'group_leader' and customer.created_by.group_leader != request.user:
        messages.error(request, '您只能查看本组的客户')
        return redirect('customerlist')

    # 获取与客户相关的评论
    comments = customer.comments.all()

    # 如果是 POST 请求，则处理评论添加逻辑
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                customer=customer,
                content=content,
                created_by=request.user,
            )
            messages.success(request, "评论添加成功")
            return redirect('customer_detail_mobile', id=customer.id)
        else:
            messages.error(request, "评论内容不能为空")

    return render(request, 'mobile/mobile_sub/customer_detail.html', {
        'customer': customer,
        'comments': comments,
    })

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def add_comment_ajax(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            content = body.get("content")
            customer_id = body.get("customer_id")

            if not content or not customer_id:
                return JsonResponse({"success": False, "error": "缺少必要参数"}, status=400)

            try:
                customer = Customer.objects.get(id=customer_id)
                comment = Comment.objects.create(
                    customer=customer,
                    content=content,
                    created_by=request.user,
                )
                return JsonResponse({
                    "success": True,
                    "comment": {
                        "content": comment.content,
                        "created_by": request.user.username,
                        "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    },
                })
            except Customer.DoesNotExist:
                return JsonResponse({"success": False, "error": "客户不存在"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "无效的JSON数据"}, status=400)
    return JsonResponse({"success": False, "error": "无效请求方法"}, status=405)