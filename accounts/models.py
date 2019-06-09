from django.db import models

# Create your models here.
class Account(models.Model):

    uphone = models.CharField(max_length=11)
