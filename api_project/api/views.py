from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
