from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    return render(request,'views/admin_view.html')