# Generated by Django 2.2 on 2019-05-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
    ]
