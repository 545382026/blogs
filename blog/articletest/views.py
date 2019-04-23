from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse('首页')