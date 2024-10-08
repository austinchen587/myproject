from rest_framework import serializers
from .models import Customer
from sales.models import SalesUser  # 引入 SalesUser 模型

class CustomerSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)  # 获取创建人的用户名
    updated_by = serializers.CharField(source='updated_by.username', read_only=True)  # 获取最后修改人的用户名
    class Meta:
        model = Customer
        fields = '__all__'  # 包含所有字段

    def create(self, validated_data):
        # 获取当前请求的用户
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
            validated_data['updated_by'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 更新时设置最后修改人
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['updated_by'] = request.user
        return super().update(instance, validated_data)