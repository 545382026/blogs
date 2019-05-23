from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import  HttpResponse
from django.views.generic import View
from .models import Comment, Article
from .forms import CommentForm
# Create your views here.

class AddComment(View):
    def post(self, request, id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm(request.POST)
        if cf.is_valid():
            username = cf.cleaned_data['name']
            email = cf.cleaned_data['email']
            url = cf.cleaned_data['url']
            comment = cf.cleaned_data['comment']

        # username = request.POST.get('name')
        # email = request.POST.get('email')
        # url = request.POST.get('url')
        # comment = request.POST.get('comment')

            c = Comment()
            c.username = username
            c.email = email
            c.url = url
            c.content = comment
            c.article = article
            c.save()

            return redirect(reverse('blogsapp:single', args=(id,)))
        else:
            return HttpResponse('输入不合法')