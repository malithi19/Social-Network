from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm
from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer, \
    PostSerializer, LikeSerializer, TagSerializer, FeedSerializer
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import PostForm
from django.contrib.auth.models import User
from django.db.models import Q

# Regular view functions
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


def menu(req, pid):
    return render(req, "menu.html", {'pid': pid})


def edit_profile(req, pid):
    return render(req, "edit-profile.html",{'pid': pid})

def friends(request):
    user_profile = request.user.profile
    friend_ids = user_profile.friends.values_list('id', flat=True)
    users = User.objects.exclude(id=request.user.id).exclude(id__in=friend_ids)
    friends = user_profile.friends.all()
    context = {
        'users': users,
        'friends': friends
    }
    return render(request, "friends.html", context)


def add_friend(request, user_id):
    if request.method == "POST":
        friend = User.objects.get(id=user_id)
        request.user.profile.friends.add(friend)
        return redirect('profile', user_id=request.user.id)

def logout(request):
    auth_logout(request)
    return redirect('sign_in')

def messages(req):
    return render(req, "messages.html")

def newsfeed(req):
    posts = Post.objects.all().order_by('-created_at')
    return render(req, 'newsfeed.html', {'posts': posts})

def post(req,pid):
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


def other_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user
    }
    return render(request, 'other_profile.html', context)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save tags and other ManyToMany fields

            post_data = {
                'content': post.content,
                'image': post.image.url if post.image else None,
                'created_at': post.created_at.isoformat(),
                'author': {
                    'username': post.author.username,
                    'profile_picture': post.author.profile_picture.url
                }
            }

            return JsonResponse({'success': True, 'post': post_data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def user_list(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()
    
    context = {
        'users': users,
        'query': query
    }
    return render(request, 'user_list.html', context)

def user_search(request):
    query = request.GET.get('q', '')
    search_results = User.objects.none()  # Initialize with empty queryset
    if query:
        search_results = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    
    context = {
        'users': User.objects.all(),
        'search_results': search_results,
        'query': query,
    }
    return render(request, 'user_list.html', context)

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