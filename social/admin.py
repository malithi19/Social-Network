#Django models defined in application
from django.contrib import admin
from . models import Post, Comment, Tag, Mention, UserProfile, Photo, Friendship, Like, Feed

#register django models
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Mention)
admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(Friendship)
admin.site.register(Like)
admin.site.register(Feed)

