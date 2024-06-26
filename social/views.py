from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer
from .forms import SignUpForm
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer, \
    PostSerializer, LikeSerializer, TagSerializer, FeedSerializer,UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User

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


"""def sign_up(req):
    return render(req, "sign up.html")"""


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('sign_in')  # Redirect to the profile page after sign up
    else:
        form = SignUpForm()
    return render(request, 'sign up.html', {'form': form})


"""def sign_in(req):
    return render(req, "sign_in.html")"""



def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f'Username: {username}, Password: {password}')  # Debug print statement
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('newsfeed')
            else:
                print('Authentication failed')  # Debug print statement
        else:
            print('Form is not valid')  # Debug print statement
        return render(request, 'sign_in.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
        return render(request, 'sign_in.html', {'form': form})


def forgot_password(req):
    return render(req, "forgotten_password.html")


def other_profile(req):
    return render(req, "other_profile.html")

#CommentViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        if post_id:
            return self.queryset.filter(post_id=post_id)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

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
