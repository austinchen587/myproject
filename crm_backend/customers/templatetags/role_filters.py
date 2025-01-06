from django import template

register = template.Library()

@register.filter
def has_role(user, roles):
    """
    检查用户是否有指定的角色。
    :param user: 用户对象
    :param roles: 逗号分隔的角色字符串 (如 'assistant,assistant_leader')
    :return: 如果用户的角色在 roles 中返回 True，否则返回 False
    """
    if not hasattr(user, 'role'):
        return False  # 如果用户对象没有 role 属性，返回 False
    return user.role in roles.split(',')