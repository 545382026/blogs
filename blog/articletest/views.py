from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Public, Kind, Lable
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