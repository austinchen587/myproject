from django import template

register = template.Library()

@register.filter
def repeat(value, times):
    """
    Repeats the given string a specified number of times.
    :param value: The string to repeat
    :param times: The number of repetitions
    :return: Repeated string
    """
    try:
        times = int(times)
        return value * times
    except (ValueError, TypeError):
        return value