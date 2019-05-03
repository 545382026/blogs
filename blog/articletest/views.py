from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Public, Kind, Lable
import markdown
# Create your views here.

def index(request):
    art = Article.objects.all()
    kind = Kind.objects.all()[:3]
    arts = Article.objects.all()[:3]
    lable = Lable.objects.all()
    archive_list=Article.objects.ditinct_date()
    print(archive_list)
    con = {'article':art, 'kind':kind, 'arts':arts, 'lable':lable, 'archive':archive_list}
    return render(request, 'articletest/index.html', con)

def single(request, id):
    art = Article.objects.get(pk=id)
    # 第一种直接利用Markdown 生成html
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
    emile = request.POST['emile']
    url = request.POST['url']
    comment = request.POST['comment']

    pub = Public.objects.all()
    pub.pname = name
    pub.pemile = emile
    pub.purl = url
    pub.pcontent = comment
    pub.paid = id

    pub.save()



    return redirect(request('articletest/single/'+id+"/"))
