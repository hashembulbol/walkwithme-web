from dataclasses import fields
import profile
from turtle import update
from urllib.request import Request
from rest_framework import serializers
from .models import Profile, Post, FriendRequest
from django.contrib.auth.hashers import make_password

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

# class RoutineSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()

#     class Meta:
#         model = Routine
#         fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1

    def create(self, validated_data):

        profile = Profile.objects.create(
        username=validated_data['username'],
        password = make_password(validated_data['password']),
        )
        return profile
    
    def update(self, instance, validated_data):
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return super().update(instance, validated_data)
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
        

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'
        depth = 1
       
        
    
