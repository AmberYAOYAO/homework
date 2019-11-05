from django import template

register = template.Library() #实例化Django模板库

@register.filter# 注册过滤器
def uper(obj):
    return obj.upper()

@register.filter
def get_filter(obj):
    result = obj.goods_set.filter(statue = 1)[:4]
    return result

@register.filter
def get_four(obj):
    return obj[:4]

@register.filter("set_url")
def set_url(obj,a):
    return obj.replace(a,"")

@register.filter("set_phone")
def set_phone(obj):
    result = obj[:3]+"****"+obj[7:]
    return result