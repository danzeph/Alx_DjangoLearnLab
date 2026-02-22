from django.urls import include, path
from api.views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'book_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList View (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router urls for BookViewset - CRUD operatons 
    # All routers are auto-generated because of the router
    path('', include(router.urls)) 
]
