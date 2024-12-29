from django import template

register = template.Library()

@register.filter
def get_tag_name(tags, tag_id):
    """
    根据标签 ID 返回标签名称
    """
    # 遍历字典列表，找到匹配的标签
    tag = next((tag for tag in tags if str(tag["id"]) == str(tag_id)), None)
    return tag["name"] if tag else "未知标签"