from django.urls import path, reverse_lazy

from .admin_view import admin_view
from .librarian_view import  librarian_view
from .member_view import member_view
from . import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name = 'logout'),
    path('books/', views.list_books, name='book-list'),
    path('books/library/', views.LibraryDetailView.as_view(), name='books-details'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
