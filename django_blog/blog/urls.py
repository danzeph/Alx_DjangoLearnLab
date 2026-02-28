from django.urls import path
from .views import profile_update, register, profile_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/',register , name='register'),
    path('login/',LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view() , name='logout'),
    path('profile/',profile_update, name='profile'),
    


    # path('', 'blog.home.html'),
    # path('', 'blog.home.html'),
    # path('', 'blog.home.html'),
]