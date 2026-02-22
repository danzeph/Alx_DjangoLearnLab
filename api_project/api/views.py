from django.shortcuts import render
from rest_framework import generics
from api.models import Book
from api.serializers import BookSerializer

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
