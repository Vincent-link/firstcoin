# Generated by Django 2.2 on 2019-07-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20190620_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='real_pageviews',
            field=models.IntegerField(default=0, verbose_name='实际页面浏览量'),
            preserve_default=False,
        ),
    ]
