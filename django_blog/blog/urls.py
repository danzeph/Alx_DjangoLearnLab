from django.urls import path
from .views import DeleteView,UpdateView, profile_update, register,CreateView,DetailView,ListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/',register , name='register'),
    path('login/',LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='blog/logout.html') , name='logout'),
    path('profile/',profile_update, name='profile'),
    path('posts/',ListView.as_view(), name = 'post-list'),
    path('posts/new/',CreateView.as_view(), name = 'post-create'),
    path('posts/<int:pk>/',DetailView.as_view(), name = 'post-detail'),
    path('posts/<int:pk>/edit/',UpdateView.as_view(), name = 'post-update'),
    path('posts/<int:pk>/delete/',DeleteView.as_view(), name = 'post-delete'),

    ]