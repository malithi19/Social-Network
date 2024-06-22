from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets

from .models import UserProfile, Photo, Comment, Friendship, Post, Like, Tag, Feed
from .serializers import (
    UserProfileSerializer, PhotoSerializer, CommentSerializer, FriendshipSerializer,
    PostSerializer, LikeSerializer, TagSerializer, FeedSerializer
)


# Regular view functions
def profile(request):
    return render(request, "profile.html")


def edit_description(request, pid):
    return render(request, "edit_description.html", {'pid': pid})


def edit_profile(request, pid):
    return render(request, "edit_profile.html", {'pid': pid})


def friends(request, pid):
    return render(request, "friends.html", {'pid': pid})


def logout(request):
    return render(request, "logout.html")


def messages(request, pid):
    return render(request, "messages.html", {'pid': pid})


def newsfeed(request):
    return render(request, "newsfeed.html")


def settings(request, pid):
    return render(request, "settings.html", {'pid': pid})


def sign_up(request):
    return render(request, "sign_up.html")


def sign_in(request):
    if request.method == 'POST':
        # Handle sign-in logic
        pass  # Implement your sign-in logic here
    return render(request, 'sign_in.html')


def forgot_password(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        try:
            if '@' in contact:  # Assume it's an email
                user = User.objects.get(email=contact)
                send_function = send_reset_link_via_email

                # Generate a password reset token
                token = default_token_generator.make_token(user)

                # Construct the reset link
                reset_url = reverse('reset_password', kwargs={
                    'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token
                })

                # Send the reset link
                send_function(user, reset_url)

                messages.success(request, 'A reset link has been sent to your email.')
                return redirect('forgot_password')
        except User.DoesNotExist:
            messages.error(request, 'No account found with that email address.')
    return render(request, 'forgotten_password.html')


def reset_password(request, uidb64, token):
    global form
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            if request.method == 'GET':
                form = SetPasswordForm(user)
                return render(request, 'reset_password.html', {'form': form})

            elif request.method == 'POST':
                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    new_password = form.cleaned_data['new_password1']
                    confirm_password = form.cleaned_data['new_password2']

                    if new_password != confirm_password:
                        messages.error(request, "Passwords do not match.")
                        return render(request, 'reset_password.html', {'form': form})

                    if len(new_password) < 8:
                        messages.error(request, "Password must be at least 8 characters long.")
                        return render(request, 'reset_password.html', {'form': form})

                    # Save the new password
                    form.save()
                    messages.success(request, 'Your password has been reset successfully.')
                    return redirect('sign_in')
                else:
                    messages.error(request, 'Please correct the errors below.')
        else:
            messages.error(request, 'Invalid password reset link.')
            return redirect('forgot_password')

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Invalid password reset link.')
        return redirect('forgot_password')

    return render(request, 'reset_password.html', {'form': form})


def send_reset_link_via_email(user, reset_url):
    send_mail(
        'Password Reset Request',
        f'Here is the link to reset your password: {reset_url}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )


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
