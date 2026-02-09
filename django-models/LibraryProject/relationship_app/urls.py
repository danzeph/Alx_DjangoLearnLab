from django.urls import path
from .views import list_books, BookDetailView

urlpatterns = [
    path('', list_books, name='book-list'),
    path('library', BookDetailView.as_view(), name='books-details'),
    # path('library/<int:pk/', BookDetailView.as_view(), name='books-details'),

]
