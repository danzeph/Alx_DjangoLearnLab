from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Comment, Post, UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','tags']
        required_fields = ['title','content']

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) < 5:
            raise forms.ValidationError("Post content should be more that 5 characters")
        if "spam" in content:
            raise forms.ValidationError(f"forbidden words like \"spam\" not allowed in post")
        
        return content
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) <  5:
            raise forms.ValidationError("Comment must be at least 5 character long")
        if "spam" in content.lower():
            raise forms.ValidationError("Your comment contains forbidden words")
        return content
