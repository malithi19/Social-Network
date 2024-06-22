from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Regular views
urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
    path('', views.edit_description, name='edit_description'),
    path('', views.edit_profile, name='edit_profile'),
    path('', views.friends, name='friends'),
    path('', views.logout, name='logout'),
    path('', views.messages, name='messages'),
    path('', views.newsfeed, name='newsfeed'),
    path('', views.reset_password, name='reset_password'),
    path('', views.settings, name='settings'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
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
