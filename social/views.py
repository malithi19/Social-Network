from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer, PostSerializer, LikeSerializer, TagSerializer, FeedSerializer

# Regular view functions
def profile(req):
    return render(req, "profile.html")

def menu(req, pid):
    return render(req, "menu.html", {'pid': pid})

def edit_profile(req, pid):
    return render(req, "edit-profile.html",{'pid': pid})

def friends(req):
    return render(req, "friends.html")

def logout(req):
    return render(req, "logout.html")

def messages(req):
    return render(req, "messages.html")

def newsfeed(req):
    return render(req, "newsfeed.html")

def reset_password(req, pid):
    return render(req, "reset_password.html", {'pid': pid})

def settings(req, pid):
    return render(req, "settings.html", {'pid': pid})

def sign_up(req):
    return render(req, "sign up.html")

def sign_in(req):
    return render(req, "sign_in.html")

def forgot_password(req):
    return render(req, "forgotten_password.html")

def other_profile(req):
    return render(req, "other_profile.html")

# DRF viewsets
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
