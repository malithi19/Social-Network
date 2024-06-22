from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer, PostSerializer, LikeSerializer, TagSerializer, FeedSerializer
from .forms import SignUpForm

# Regular view functions
def profile(request):
    return render(request, "profile.html")

def edit_description(request, pid):
    return render(request, "edit_description.html", {'pid': pid})

def edit_profile(request, pid):
    return render(request, "edit-profile.html", {'pid': pid})

def friends(request, pid):
    return render(request, "friends.html", {'pid': pid})

def logout(request):
    return render(request, "logout.html")

def messages(request, pid):
    return render(request, "messages.html", {'pid': pid})

def newsfeed(request):
    return render(request, "newsfeed.html")

def reset_password(request, pid):
    return render(request, "reset_password.html", {'pid': pid})

def settings(request, pid):
    return render(request, "settings.html", {'pid': pid})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after sign up
    else:
        form = SignUpForm()
    return render(request, 'sign up.html', {'form': form})

def sign_in(request):
    return render(request, "sign_in.html")

def forgot_password(request):
    return render(request, "forgotten_password.html")

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