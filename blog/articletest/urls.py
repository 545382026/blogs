from django.conf.urls import url
from . import views
app_name = 'articletest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),
    url(r'^comment/(\d+)/$', views.comment, name='comment'),
]
