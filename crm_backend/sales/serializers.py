# sales/serializers.py
from rest_framework import serializers
from .models import SalesUser

class SalesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUser
        fields = ['id', 'username', 'role', 'is_active']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUser  # 指向自定义的 SalesUser 模型
        fields = ['username', 'password','role']

    def create(self, validated_data):
        # 创建新用户并设置密码
        user = SalesUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user