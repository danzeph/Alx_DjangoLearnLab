from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_member(user):
    return user.is_authenticated and user.groups.filter(name='Member').exists()

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'views/member_view.html')
