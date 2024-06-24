from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Regular views
urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
    path('menu/<int:pid>/', views.menu, name='menu'),
    path('', views.edit_profile, name='edit_profile'),
    path('friends/', views.friends, name='friends'),
    path('', views.logout, name='logout'),
    path('messages/', views.messages, name='messages'),
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('', views.reset_password, name='reset_password'),
    path('', views.settings, name='settings'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('other-profile/', views.other_profile, name='other_profile'),
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