from django.shortcuts import render, redirect
from blog.forms import RegistrationForm, UserProfileForm, UserUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blog.models import UserProfile

# class CreateUserView(CreateView):
#     template_name = "blog/register.html"
#     form_class = RegistrationForm
#     success_url = 'blog/profile'

def register(request):
    template_name = "blog/register.html"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, template_name, {"form":form})


# class ProfileView(LoginRequiredMixin,DetailView):
#     """Commented out to handle update_form, and profile_form"""
#     template_name = 'blog/profile.html'
#     model = UserProfile

#     # def get_object(self):
#     #     return self.request.user.profile

@login_required
def profile_update(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "blog/profile.html", context)

@login_required
def profile_view(request):
    instance, _ = UserProfile.objects.get_or_create(user=request.user)
    template_name = 'blog/profile.html'
    context={'profile': instance}
    return render(request,template_name, context)
