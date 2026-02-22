from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Model Viewset class to do CRUD operations
class BookViewset(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
