from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    if user.userprofile.role != "librarian":
        return False
    return True

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'views/librarian_view.html')
