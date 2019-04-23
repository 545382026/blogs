from django.contrib import admin
from .models import Article, Public, Lable, Kind
# Register your models here.
admin.site.register(Lable)
admin.site.register(Kind)
admin.site.register(Article)
admin.site.register(Public)
