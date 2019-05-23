from django import template
from ..models import Article, Category, Tag

register = template.Library()
# 自定义过滤器
@register.filter(name='mylower')
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value, length):
    return value[:length]

# 自定义标签
@register.simple_tag(name='getcategorys')
def getcategorys():
    return Category.objects.all()

@register.simple_tag(name='newarticle')
def newarticle(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag(name='all_lable')
def all_lable():
    return Tag.objects.all()

@register.simple_tag
def getarchives(num=3):
    return Article.objects.dates('create_time', 'month', order='DESC')[:num]