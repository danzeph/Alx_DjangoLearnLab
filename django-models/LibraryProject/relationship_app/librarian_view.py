from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    if user.userprofile.role != "Librarian":
        return False
    return True

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')
