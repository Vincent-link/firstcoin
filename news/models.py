from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    avatar = models.ImageField(upload_to = "reporters/avatars/%Y%m", verbose_name="上传图片", default='')
    intro = models.CharField(max_length=140)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    cover = models.ImageField(upload_to = "articles/covers/%Y%m", verbose_name="上传图片", default='', max_length=500)
    content = RichTextUploadingField(default='', verbose_name='详细介绍')
    pageviews = models.IntegerField(verbose_name='页面浏览量')

    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
