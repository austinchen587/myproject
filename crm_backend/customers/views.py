from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwnerOrGroupLeader  # 自定义权限
from django.utils.dateparse import parse_date
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwnerOrGroupLeader]

    def get_queryset(self):
        user = self.request.user
        queryset = Customer.objects.all()

        # 根据用户角色筛选
        if user.role == 'admin':
            queryset = Customer.objects.all()
        elif user.role == 'group_leader':
            queryset = Customer.objects.filter(Q(created_by=user) | Q(created_by__group_leader=user))
        else:
            queryset = Customer.objects.filter(created_by=user)

        # 获取筛选参数
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        sort_field = self.request.query_params.get('sort_field', 'created_at')
        sort_direction = self.request.query_params.get('sort_direction', 'asc')

        # 解析日期并设置默认值
        try:
            # 如果没有传递 start_date，默认使用当月的第一天
            if start_date:
                start_datetime = make_aware(datetime.combine(parse_date(start_date), datetime.min.time()))
            else:
                first_day_of_month = datetime.today().replace(day=1)
                start_datetime = make_aware(datetime.combine(first_day_of_month, datetime.min.time()))

            # 如果没有传递 end_date，默认使用当前时间
            if end_date:
                end_datetime = make_aware(datetime.combine(parse_date(end_date), datetime.max.time()))
            else:
                end_datetime = make_aware(datetime.combine(datetime.today(), datetime.max.time()))

            # 验证开始日期是否在结束日期之前
            if start_datetime > end_datetime:
                return Response({"error": "开始日期不能晚于结束日期"}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError) as e:
            return Response({"error": f"日期格式不正确，请输入正确的日期格式: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        # 进行时间范围筛选
        queryset = queryset.filter(created_at__gte=start_datetime, created_at__lte=end_datetime)

        # 处理排序
        if sort_field and sort_direction:
            if sort_direction == 'desc':
                sort_field = f'-{sort_field}'  # 负号表示降序
            queryset = queryset.order_by(sort_field)

        return queryset

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_customer(request):
    if request.method == 'POST':
        data = request.data.copy()
        
        # 设置创建者和修改者
        data['created_by'] = request.user.id
        data['updated_by'] = request.user.id

        # 使用自定义序列化器，并确保 context 传递了 request
        serializer = CustomerSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            customer = serializer.save()
            return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # 打印错误，方便调试
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)