from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Regular views
from .views import create_post

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('menu/<int:pid>/', views.menu, name='menu'),
    path('', views.edit_profile, name='edit_profile'),
    path('friends/', views.friends, name='friends'),
    path('add_friend/<int:user_id>/', views.add_friend, name='add_friend'),
    path('logout/', views.logout, name='logout'),
    path('messages/', views.messages, name='messages'),
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('create_post/', create_post, name='create_post'),
    path('', views.reset_password, name='reset_password'),
    path('', views.settings, name='settings'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('users/', views.user_list, name='user_list'),
    path('other_profile/<int:user_id>/', views.other_profile, name='other_profile'),
    path('user_search/', views.user_search, name='user_search'),
]

# DRF viewsets
router = DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'photos', views.PhotoViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'friendships', views.FriendshipViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'feeds', views.FeedViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]