from django.urls import path
from .views import PostDeleteView, PostUpdateView, profile_update, register, PostCreateView, PostDetailView, PostListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/',register , name='register'),
    path('login/',LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='blog/logout.html') , name='logout'),
    path('profile/',profile_update, name='profile'),
    path('posts/', PostListView.as_view(), name = 'post-list'),
    path('posts/new/', PostCreateView.as_view(), name = 'post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),

    ]