from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('register/',views.RegisterUserView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.py'), name = 'logout'),
    path('books/', views.list_books, name='book-list'),
    path('books/library/', views.LibraryDetailView.as_view(), name='books-details'),
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
