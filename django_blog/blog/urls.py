from django.urls import path
from .views import ( 
    PostDeleteView,PostUpdateView, 
    profile_update, register, 
    PostCreateView, PostDetailView, 
    PostListView, CommentCreateView, 
    CommentDeleteView, 
    CommentUpdateView )

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/',register , name='register'),
    path('login/',LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='blog/logout.html') , name='logout'),
    path('profile/',profile_update, name='profile'),
    path('posts/',PostListView.as_view(), name = 'post-list'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('posts/<int:post_id>/comments/new/',CommentCreateView.as_view(), name = 'new-comment'),
    path('posts/<int:post_id>/comments/edit/<int:pk>/', CommentUpdateView.as_view(), name = 'edit-comment'),
    path('posts/<int:post_id>/comments/delete/<int:pk>/',CommentDeleteView.as_view(), name = 'delete-comment'),
    ]