from django.conf.urls import url, include
from . import views
from . import feed
app_name = 'blogsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),

    url(r'^archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),

    url(r'^rss/$', feed.BlogFeed(), name='rss'),
    url(r'^contact/$', views.contact, name='contact'),
    # 添加轮播图
    url(r'^ads/$', views.ads, name='ads')
]