from django.http import Http404
from django.shortcuts import redirect, render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User


def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books':books})


class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'library'
    def get_object(self):
        obj = Library.objects.first()
        if not obj:
            raise Http404("No Library object found")
        return obj
    


def register(request):
    template_name = 'relationship_app/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request,template_name,{'form':form})
