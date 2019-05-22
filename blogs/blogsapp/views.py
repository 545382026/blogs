from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def single(request, id):
    return render(request, 'single.html')