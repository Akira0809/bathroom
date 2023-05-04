from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Data(models.Model):
    big = ArrayField(models.IntegerField(default=0), default=list)
    small = ArrayField(models.IntegerField(default=0), default=list)

class User(models.Model):
    name = models.CharField(max_length=255, default="akira")
    button = models.CharField(max_length=3)