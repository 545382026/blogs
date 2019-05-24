from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article, Category, Tag, MessageInfo, Ads
from django.core.paginator import Paginator
import markdown
from comments.forms import CommentForm
from blogsapp.forms import MessageForm
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings

# Create your views here.


def index(request):
    # 页码
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum==None else pagenum

    # 得到所有文章
    articles = Article.objects.all().order_by('-views')

    # 每一页包含多少条信息
    paginator = Paginator(articles, 2)

    # 传入页码得到一个页面 page包含所有信息
    page = paginator.get_page(pagenum)

    return render(request, 'index.html', locals())


def single(request, aid):
    article = get_object_or_404(Article, pk=aid)
    # 阅读次数
    article.views += 1
    article.save()

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
    cf = CommentForm()
    return render(request, 'single.html', locals())

# 归档
def archives(request, year, month):
    # 页码
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    articles = Article.objects.filter(create_time__year=year,create_time__month=month)

    # 每一页包含多少条信息
    paginator = Paginator(articles, 2)

    # 传入页码得到一个页面 page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/archives/%s/%s/" % (year, month)
    return render(request,'index.html', locals())

#分类
def category(request, id):
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Category, pk=id).article_set.all()

    paginator = Paginator(articles, 2)
    page = paginator.get_page(pagenum)
    page.parms = '/category/%s/' % id
    return render(request, 'index.html', locals())

# 标签云
def tag(request, id):
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Tag, pk=id).article_set.all()

    paginator = Paginator(articles, 2)
    page = paginator.get_page(pagenum)
    page.parms = '/tag/%s/' % id
    return render(request, 'index.html', locals())

# 发送邮件
def contact(request):
    if request.method == 'GET':
        cf = MessageForm()
        return render(request, 'contact.html', locals())
    elif request.method == 'POST':

        try:
            send_mail(request.POST['subject'], request.POST['info'], settings.DEFAULT_FROM_EMAIL, [request.POST['email']])
        except Exception as e:
            print(e)
        message = MessageForm(request.POST)
        message.save()
        message = MessageForm()
        return render(request, 'contact.html')


def ads(request):
    if request.method == 'GET':
        return render(request, 'ads.html')
    elif request.method == 'POST':
        header = request.FILES['header']
        desc = request.POST['desc']
        user = Ads(img=header, desc=desc)
        user.save()
        return redirect(reverse('blogsapp:index'))

