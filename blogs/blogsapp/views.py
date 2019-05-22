from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article
from django.core.paginator import Paginator
import markdown
# Create your views here.


def index(request):
    # 页码
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum==None else pagenum
    print(pagenum, '__________________________')

    # 得到所有文章
    articles = Article.objects.all().order_by('-views')
    print(articles, '++++++++++++++++++++++++++')
    # 每一页包含多少条信息
    paginator = Paginator(articles, 2)
    print(paginator, '############################')
    # 传入页码得到一个页面 page包含所有信息
    page = paginator.get_page(pagenum)
    print(page, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return render(request, 'index.html', locals())


def single(request, aid):
    article = get_object_or_404(Article, pk=aid)

    # 使用MarkDown处理body 将Markdown语发转换为html标签

    # 第一种只针对某个字符串转换
    # article.body = markdown.markdown(article.body, extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc'
    # ])

    # 第二种如果在外部使用目录 需要使用构造函数的写法
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    article.body = md.convert(article.body)
    article.toc = md.toc
    return render(request, 'single.html', locals())