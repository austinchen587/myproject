# sales/views.py
from rest_framework import viewsets
from .models import SalesUser  # 从模型中导入 SalesUser
from .serializers import SalesUserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

# 生成 JWT Token 的方法
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# SalesUser 的视图集，用于处理 SalesUser 相关的 API
class SalesUserViewSet(viewsets.ModelViewSet):
    queryset = SalesUser.objects.all()
    serializer_class = SalesUserSerializer

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role', 'user')
        group_leader_id = request.data.get('group_leader')

        if not username or not password:
            return Response({'error': '用户名和密码是必填项。'}, status=status.HTTP_400_BAD_REQUEST)

        if SalesUser.objects.filter(username=username).exists():
            return Response({'error': '用户名已存在。'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group_leader = SalesUser.objects.get(id=group_leader_id) if group_leader_id else None
            user = SalesUser.objects.create_user(
                username=username,
                password=password,
                role=role,
                group_leader=group_leader
            )
            tokens = get_tokens_for_user(user)
            return Response({
                'message': '注册成功',
                'access_token': tokens['access'],
                'refresh_token': tokens['refresh'],
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'role': user.role,
                    'group_leader': user.group_leader.id if user.group_leader else None,
                }
            }, status=status.HTTP_201_CREATED)
        except SalesUser.DoesNotExist:
            return Response({'error': '指定的组长不存在。'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 登录视图，用于用户登录
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({
            'message': 'Login successful',
            'user': username,
            'access_token': tokens['access'],
            'refresh_token': tokens['refresh']
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# 获取当前用户信息的视图
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.user.is_authenticated:
        serializer = SalesUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)