from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from .admin_view import is_admin
from .librarian_view import is_librarian
from .member_view import is_member
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request,'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')