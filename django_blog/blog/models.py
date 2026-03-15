from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    tags = TaggableManager(help_text='add tags, seperated by comma', blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')


    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pic')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.content} by {self.author}"



class Book(models.Model):
    name = models.CharField(max_length=50)
    tags = TaggableManager()

    def __str__(self):
        return self.name