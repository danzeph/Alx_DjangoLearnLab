from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import CommentForm, PostForm, RegistrationForm, UserProfileForm, UserUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment, Post, UserProfile


def register(request):
    """for registring new users.
        included fields from Usercreaion form( email, first and last name)
    """
    template_name = "blog/register.html"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
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
    """Post detail view with comments under the post"""
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object) 
        return context
    


class PostCreateView(CreateView,LoginRequiredMixin):
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/post_edit.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        """allow only author to perform this actions"""
        obj = self.get_object()
        return obj.author == self.request.user
    
    def handle_no_permission(self):
        """sends a message and redirect if no permission"""
        messages.error(self.request, "You are not the owner of this post.")
        return redirect('post-list')

    
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        """allow only author to perform this actions"""
        obj = self.get_object()
        return obj.author == self.request.user
    
    def handle_no_permission(self):
        """sends a message and redirect if no permission"""
        messages.error(self.request, "You are not the owner of this post.")
        return redirect('post-list')
    


# @login_required 
# def comment_create(request, post_pk):  
#     post = get_object_or_404(Post, pk=post_pk)  
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user 
#             comment.post = post
#             comment.save()
#             messages.success(request, "Comment added!")
#             return redirect('post-detail', pk=post_pk)
#     else:
#         form = CommentForm()
    
#     return render(request, 'blog/comment-create.html', {'form': form, 'post': post})



# create comment view view    
class CommentCreateView(LoginRequiredMixin,CreateView):
    template_name = "blog/comment_create.html"
    form_class = CommentForm
    model = Comment

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.kwargs['post_id'])
        return context
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def handle_no_permission(self):
        """sends a message and redirect if no permission"""
        messages.error(self.request, "You must be logged in to comment")
        return redirect('login')
    
    def get_success_url(self):
        messages.success(self.request, "Comment added! ")
        return  reverse_lazy('post-detail', kwargs={'pk':self.kwargs['post_id']})


# update comment view    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "blog/comment_edit.html"
    form_class = CommentForm


    def test_func(self):
        """allow only author to perform this actions"""
        obj = self.get_object()
        return obj.author == self.request.user
    

    def handle_no_permission(self):
        """sends a message and redirect if no permission"""
        messages.warning(self.request, "You are not the owner of this comment.")
        obj = self.get_object()
        return redirect('post-detail', pk = obj.post.id)

    def get_success_url(self):
        obj = self.get_object()
        messages.success(self.request, "Comment updated successfully")
        return reverse_lazy('post-detail', kwargs={'pk': obj.post.id})
    
        

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"

    def test_func(self):
        """allow only author to perform this actions"""
        obj = self.get_object()
        return obj.author == self.request.user
    
    def handle_no_permission(self):
        """sends a message and redirect if unauthored"""
        messages.warning(self.request, "You are not the owner of this comment.")
        obj = self.get_object()
        return redirect('post-detail', pk = obj.post.pk)

    def get_success_url(self):
        obj = self.get_object()
        messages.success(self.request, "Comment updated successfully")
        return reverse_lazy('post-detail', kwargs={'pk': obj.post.pk})
