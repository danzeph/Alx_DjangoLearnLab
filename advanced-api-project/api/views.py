from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from api.models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.response import Response

class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title','publication_year']
    search_fields = ['title',]
    filterset_fields = ['title', 'author', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]



    def get_queryset(self):
        """Custom method to filter based on book title"""
        """Custom filters based on URL only"""
        queryset = Book.objects.all()
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
        return queryset


class DetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        # 1. Initialize serializer with request data
        serializer = self.get_serializer(data=request.data)
        
        # 2. Validate data
        serializer.is_valid(raise_exception=True)
        
        # 3. Perform the actual creation (calls perform_create)
        self.perform_create(serializer)
        
        # 4. Return a custom response
        return Response(
            {"message": "Custom success message", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

class UpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


