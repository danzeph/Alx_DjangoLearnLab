from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name = 'logout'),
    path('', views.list_books, name='book-list'),
    path('books/library/', views.LibraryDetailView.as_view(), name='books-details'),
    path('admin_only/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
