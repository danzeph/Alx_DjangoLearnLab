from django.urls import path
from .views import profile_update, register, profile_view

urlpatterns = [
    path('register/',register , name='register'),
    path('profile/',profile_update, name='profile'),
    # path('profile/<int:pk>/update',UpdateProfileView.as_view(), 'profile'),


    # path('', 'blog.home.html'),
    # path('', 'blog.home.html'),
    # path('', 'blog.home.html'),
]