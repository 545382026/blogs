from django.db import models

# Create your models here.
class Lable(models.Model):
    label = models.CharField(max_length=20, verbose_name='总标签')
    def __str__(self):
        return self.label

class Kind(models.Model):
    kind = models.CharField(max_length=100)
    def __str__(self):
        return self.kind

# 文章归档
class ArticleManager(models.Manager):
    def ditinct_date(self):
        disinct_date_list =[]
        date_list = self.values('atime')
        for date in date_list:
            date = date['atime'].strftime('%Y{y}%m{m}').format(y='年', m='月')
            if date not in disinct_date_list:
                disinct_date_list.append(date)
        return disinct_date_list

class Article(models.Model):
    atitle = models.CharField(max_length=50, verbose_name='文章标题')
    akind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name='类别')
    atime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    auser = models.CharField(max_length=20, verbose_name='发布人')
    anum = models.IntegerField(default=0, verbose_name='阅读次数')
    alabel = models.ForeignKey(Lable,on_delete=models.CASCADE, verbose_name='标签外键')
    acontent = models.TextField(verbose_name='文章内容')
    objects = ArticleManager()

    def __str__(self):
        return self.atitle

class Public(models.Model):
    pname = models.CharField(max_length=50, verbose_name='评论人')
    pemile = models.EmailField(max_length=254, verbose_name='邮箱')
    purl = models.URLField(max_length=200, verbose_name='网址')
    pcontent = models.TextField(verbose_name='评论内容')
    ptime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    paid = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.pname




