from email.policy import HTTP
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from .models import FriendRequest, Profile, Post
from .serializers import PostSerializer, ProfileSerializer, RequestSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404




class ProfileAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many = True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




class ProfileDetailsAPIView(APIView):
    def get_object(self, username):
        try:
            return Profile.objects.get(username=username)
        except Profile.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
                
    def get(self, request, username):
        article = self.get_object(username)
        serializer = ProfileSerializer(article)
        return Response(serializer.data)

    def put(self, request, username):

        serializer = ProfileSerializer(self.get_object(username), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        profile = self.get_object(username)
        profile.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class AuthenticateAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            
            # `django.contrib.auth.User` instance
            'user': str(request.user),
            
            
            # None
            'auth': str(request.auth),
        }

        
        return Response(content)



class PostsAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request, username):
       
        
        request.data['author'] = Profile.objects.get(username=username)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CreatePostsAPIView(APIView):
    def get(self, request, username, content):
        profile = Profile.objects.get(username=username)
        post = Post.objects.create(author= profile, content= content)
        return Response(status=status.HTTP_201_CREATED)

class DeletePostAPIView(APIView):
    def get(self, request, id):
        post = Post.objects.get(id=id).delete()
        return Response(status.HTTP_204_NO_CONTENT)


class RequestsAPIView(APIView):

    def get(self, request, sender, receiver):
        
        senderProfile = Profile.objects.get(username=sender)
        receiverProfile = Profile.objects.get(username=receiver)
        
        freq = FriendRequest.objects.create(sender = senderProfile, receiver = receiverProfile)
        
        
        return Response(status=status.HTTP_201_CREATED)
    
class GetAllRequestsAPIView(APIView):

    def get(self, request):
        reqs = FriendRequest.objects.all()
        serializer = RequestSerializer(reqs, many = True)
        return Response(serializer.data)


class DeleteRequestAPIView(APIView):
    def delete(self, request, id):
        req = FriendRequest.objects.get(id=id)
        req.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class AcceptReqAPIView(APIView):
    def get(self, request, id):
        req = FriendRequest.objects.get(id=id)
        req.sender.friends.add(req.receiver)
        req.receiver.friends.add(req.sender)
        req.delete()
        return Response(status.HTTP_201_CREATED)

class RejectReqAPIView(APIView):
    def get(self, request, id):
        req = FriendRequest.objects.get(id=id)
        req.delete()
        return Response(status.HTTP_201_CREATED)

class DeleteFriendAPIView(APIView):
    def get(self, request, deleter, deleted):
        deleter = Profile.objects.get(username=deleter)
        deleter.friends.remove(deleted)
        Profile.objects.get(id=deleted).friends.remove(deleter)
        return Response(status.HTTP_204_NO_CONTENT)

class GetFriendsAPIView(APIView):
    def get(self, request, username):
        friends = Profile.objects.get(username=username).friends
        serializer = ProfileSerializer(friends, many = True)
        return Response(serializer.data)

    