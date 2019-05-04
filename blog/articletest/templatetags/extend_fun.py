from django import template
from ..models import Article
# 得到django 负责管理标签和过滤器的类
register = template.Library()

@register.simple_tag
def getlatestarticle():
    latearticle = Article.objects.all().order_by("-atime")
    return latearticle