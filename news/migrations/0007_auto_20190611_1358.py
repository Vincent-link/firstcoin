# Generated by Django 2.2 on 2019-06-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_article_pageviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pageviews',
            field=models.IntegerField(verbose_name='页面浏览量'),
        ),
    ]
