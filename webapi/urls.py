from django.contrib import admin
from django.urls import path

from webapi.views import CreatePostsAPIView,DeletePostAPIView, ProfileAPIView,GetAllRequestsAPIView, ProfileDetailsAPIView, AuthenticateAPIView, PostsAPIView, RequestsAPIView, RejectReqAPIView, AcceptReqAPIView, DeleteRequestAPIView, DeleteFriendAPIView, GetFriendsAPIView

urlpatterns = [
    
    path('profile/', ProfileAPIView.as_view()),
    path('profile/<str:username>/', ProfileDetailsAPIView.as_view()),
    path('authenticate/', AuthenticateAPIView.as_view()),
    path('posts/', PostsAPIView.as_view()),
    path('deletepost/<int:id>', DeletePostAPIView.as_view()),

    path('createpost/<str:username>/<str:content>/', CreatePostsAPIView.as_view()),
    path('friendrequests/<str:sender>/<str:receiver>/', RequestsAPIView.as_view()),
    path('friendrequests/', GetAllRequestsAPIView.as_view()),
    path('friendrequests/<int:id>/', DeleteRequestAPIView.as_view()),
    path('acceptreq/<int:id>/', AcceptReqAPIView.as_view()),
    path('rejectreq/<int:id>/', RejectReqAPIView.as_view()),
    path('deletefriend/<str:deleter>/<int:deleted>/', DeleteFriendAPIView.as_view()),
    path('getfriends/<str:username>/', GetFriendsAPIView.as_view()),


    

]