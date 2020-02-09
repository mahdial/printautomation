from django import template

register = template.Library()

@register.filter
def replaceSlash(value):
    return value.replace("\\", '/')