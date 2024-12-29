from django import template

register = template.Library()

@register.filter
def lower(value):
    """
    将字符串转换为小写
    :param value: 输入值
    :return: 转换为小写的字符串或原值
    """
    if isinstance(value, str):
        return value.lower()
    return value  # 如果不是字符串，直接返回原值

@register.filter
def endswith(value, arg):
    """
    检查字符串是否以指定的后缀结尾
    :param value: 输入字符串
    :param arg: 后缀字符串
    :return: 如果以指定后缀结尾，返回 True；否则返回 False
    """
    if not isinstance(value, str):
        return False  # 如果 value 不是字符串，返回 False
    if not isinstance(arg, str):
        raise ValueError("endswith 参数必须是字符串")  # 确保后缀是字符串
    return value.lower().endswith(arg.lower())  # 忽略大小写比较

