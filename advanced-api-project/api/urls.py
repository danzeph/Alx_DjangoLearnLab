from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('books/', views.ListView.as_view(),name ='books'),
    path('books/create', views.CreateView.as_view(), name='create-books'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/delete/', views.DeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/update/', views.UpdateView.as_view(), name='book-update'),
    path('c', obtain_auth_token),
]
