from django.http import Http404
from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books':books})


class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    def get_object(self):
        obj = Library.objects.first()
        if not obj:
            raise Http404("No Library object found")
        return obj
    
    
