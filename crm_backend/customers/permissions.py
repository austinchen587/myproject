from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwnerOrAdmin(BasePermission):
    """
    仅允许客户的创建者或管理员进行修改和查看。
    """

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj.created_by == request.user

class IsGroupLeaderOrAdmin(BasePermission):
    """
    组长和管理员可以修改和查看客户信息。
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'admin' or 
            request.user.role == 'group_leader' or 
            obj.created_by == request.user or 
            obj.created_by.group_leader == request.user
        )
    
class IsAdminOrOwnerOrGroupLeader(permissions.BasePermission):
    """
    允许管理员查看、修改和删除所有客户信息。
    组长可以查看、修改、删除自己的客户以及组员的客户。
    普通用户只能查看和修改自己的客户。
    """

    def has_object_permission(self, request, view, obj):
        # 如果是管理员，允许所有权限
        if request.user.role == 'admin':
            return True
        # 如果是组长，允许修改自己的客户和组员的客户
        elif request.user.role == 'group_leader':
            return obj.created_by == request.user or obj.created_by.group_leader == request.user
        # 普通用户只能修改自己的客户
        return obj.created_by == request.user