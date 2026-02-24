from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter,SearchFilter
from api.models import Book
from .serializers import AuthorSerializer, BookSerializer

class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['author__name']
    search_fields = ['title']


    def get_queryset(self):
        """Custom method to filter based on book title"""
        """Custom filters based on URL"""
        queryset = Book.objects.all()
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
        return queryset


class DetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class UpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


