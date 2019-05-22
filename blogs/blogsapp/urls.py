from django.conf.urls import url, include
from . import views
app_name = 'blogsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single')
]