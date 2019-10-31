from django import template

register = template.Library() #实例化Django模板库

@register.filter# 注册过滤器
def uper(obj):
    return obj.upper()
@register.filter
def get_four(obj):
    return obj[:4]