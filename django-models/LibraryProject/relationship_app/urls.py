from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, RegisterUserView, UserLogoutView

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('register/',RegisterUserView.as_view(), name='register'),
    path('logout/',UserLogoutView.as_view(), name = 'logout'),
    path('books/', list_books, name='book-list'),
    path('books/library/', LibraryDetailView.as_view(), name='books-details'),
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
