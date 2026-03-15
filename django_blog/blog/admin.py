from django.contrib import admin

from blog.models import Comment, UserProfile,Post, Book

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Book)

