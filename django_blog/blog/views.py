from django.shortcuts import render, redirect
from blog.forms import PostForm, RegistrationForm, UserProfileForm, UserUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from blog.models import Post, UserProfile


def register(request):
    """for registring new users.
        included fields from Usercreaion form( email, first and last name)
    """
    template_name = "blog/register.html"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, template_name, {"form":form})




@login_required
def profile_update(request):

    profile, _ = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
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



class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    model = Post

class PostCreateView(CreateView,LoginRequiredMixin):
    form_class = PostForm
    template_name = "blog/post_create.html"
    model = Post
    # success_url = '/blog/home/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = 'blog/post_edit.html'
    context_object_name = 'post'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = 'post-list'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = 'blog/post_edit.html'
    context_object_name = Post.objects.all()
    form_class = PostForm
    # success_url = '/blog/home/'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user