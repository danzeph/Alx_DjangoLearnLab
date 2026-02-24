from django.shortcuts import render
from rest_framework import generics #, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter,SearchFilter
from api.models import Book
from .serializers import BookSerializer
# from rest_framework.response import Response

class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['title','publication_year']
    search_fields = ['title', 'author']
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
    
    # def create(self, request, *args, **kwargs):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(
    #         {
    #             "message":"Book created successfully",  
    #             "data":serializer.data
    #         }, 
    #         status=status.HTTP_201_CREATED
    #         )

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)

class UpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


