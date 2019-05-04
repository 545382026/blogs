from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Public, Kind, Lable
import markdown
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    art = Article.objects.all()
    # 分页器
    paginator = Paginator(art, 2)
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    page = paginator.page(pagenum)


    kind = Kind.objects.all()[:3]
    arts = Article.objects.all()[:3]
    lable = Lable.objects.all()
    archive_list = Article.objects.ditinct_date()
    print(archive_list)
    con = {'page':page, 'kind':kind, 'arts':arts, 'lable':lable, 'archive':archive_list}
    return render(request, 'articletest/index.html', con)

def single(request, id):
    art = Article.objects.get(pk=id)
    # # 第一种直接利用Markdown 生成html
    # art.acontents = markdown.markdown(art.acontents, extensions = [
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc'
    # ])
    # 第二种
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    art.acontents = md.convert(art.acontents)
    art.toc = md.toc

    num = len(Article.objects.get(pk=id).public_set.all())
    kind = Kind.objects.all()[:3]
    arts = Article.objects.all()[:3]
    lable = Lable.objects.all()
    archive_list = Article.objects.ditinct_date()
    # print(art.atitle, art.akind)
    con = {'art':art, 'kind':kind, 'arts':arts, 'lable':lable, 'archive':archive_list, 'num':num}
    return render(request, 'articletest/single.html', con)

def comment(request, id):
    # pub = Article.objects.get(pk=id).public_set.all()

    name = request.POST['name']
    emile = request.POST['email']
    url = request.POST['url']
    comment = request.POST['comment']
    pid = Article.objects.get(pk=id)
    print(name, emile, url, comment)
    pub = Public()
    pub.pname = name
    pub.pemile = emile
    pub.purl = url
    pub.pcontent = comment
    pub.paid = pid
    pub.save()

    return HttpResponseRedirect('/articletest/single/'+str(id)+"/")
