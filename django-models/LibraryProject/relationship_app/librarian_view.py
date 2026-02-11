from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    return user.is_authenticated and user.group.filter(name='Admin').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'views/librarian_view.html')
