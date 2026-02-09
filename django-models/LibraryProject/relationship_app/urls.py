from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('register/',views.RegisterUserView.as_view(), name='register'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.py'), name = 'logout'),
    path('books/', views.list_books, name='book-list'),
    path('books/library/', views.LibraryDetailView.as_view(), name='books-details'),
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
