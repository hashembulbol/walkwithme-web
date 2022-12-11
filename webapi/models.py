from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from annoying.fields import AutoOneToOneField


# Create your models here.

# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title



class Profile(AbstractUser):
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    friends = models.ManyToManyField("Profile", blank=True)
    steps = models.IntegerField(default=0)
    diet = models.TextField(default='No Specified Diet')
    maintained = models.IntegerField(default=0)
    

class Post(models.Model):
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)

class FriendRequest(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE)