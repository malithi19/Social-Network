from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer, PostSerializer, LikeSerializer, TagSerializer, FeedSerializer

# Regular view functions

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  # Assuming user is authenticated
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)

def edit_description(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: description = Description.objects.get(id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'edit_description.html', context)

def edit_profile(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: profile = Profile.objects.get(id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'edit_profile.html', context)

def friends(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: friends = Friend.objects.filter(profile_id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'friends.html', context)

def logout(request):
    return render(request, 'logout.html')

def messages(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: messages = Message.objects.filter(profile_id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'messages.html', context)

def newsfeed(request):
    # Example: posts = Post.objects.all()[:10]  # Assuming you want to show latest 10 posts
    context = {
        # Add necessary context data here
    }
    return render(request, 'newsfeed.html', context)

def reset_password(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: user = User.objects.get(id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'reset_password.html', context)

def settings(request, pid):
    # Retrieve specific data based on pid if needed
    # Example: settings = Settings.objects.get(profile_id=pid)
    context = {
        'pid': pid,
    }
    return render(request, 'settings.html', context)

def sign_up(request):
    return render(request, 'sign up.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def forgot_password(request):
    return render(request, 'forgotten_password.html')

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
