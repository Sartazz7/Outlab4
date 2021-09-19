from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    last_update = models.TimeField()

class Repository(models.Model):
    user_name = models.ManyToManyField(Profile)
    name = models.TextField(max_length=100, default='')
    stars = models.IntegerField(default=0)