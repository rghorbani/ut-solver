from django import template

register = template.Library()


@register.filter
def sub(first, second):
    return second - first