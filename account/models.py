from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.
class Data(models.Model):
    big = ArrayField(models.IntegerField(default=0), default=list)
    small = ArrayField(models.IntegerField(default=0), default=list)
    big_maximum = ArrayField(models.BooleanField(default=False), default=list)
    small_maximum = ArrayField(models.BooleanField(default=False), default=list)

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="a")
    button = models.CharField(max_length=3, default="a")

    def __str__(self):
        return f"{self.user.username}: {self.button}"