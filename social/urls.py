from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import get_friends_list, create_post, update_profile_picture, update_cover_photo, tag_friend
# Regular views
from .views import create_post
from .views import update_profile_picture
from .views import update_cover_photo

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('update_profile_picture/', update_profile_picture, name='update_profile_picture'),
    path('update_cover_photo/', update_cover_photo, name='update_cover_photo'),
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
    path('get_friends_list/', get_friends_list, name='get_friends_list'),
    path('tag_friend/', tag_friend, name='tag_friend'),
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