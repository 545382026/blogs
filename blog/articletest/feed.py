from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse
class PostFeed(Feed):
    """
    进行网站包装成XML格式
    RSS 可以把网站包装成XML格式
    可以通过RSS聚合工具订阅，该工具会回去RSS订阅更新的内容
    不要每次进入博客查看更新
    """
    title = '文章'
    description = '摘要'
    link = '/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.atitle

    def item_description(self, item):
        return item.acontent

    def item_link(self, item):
        return reverse('articletest:single', args=(item.id, ))
