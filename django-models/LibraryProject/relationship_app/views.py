from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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
    


class RegisterUserView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object) 
        return response



# class UserLoginView(LoginView):
#     template_name = 'relationship_app/login.html'
#     next_page = reverse_lazy('book-list')


# class UserLogoutView(LogoutView):
#     template_name ='relationship_app/logout.html'
    
