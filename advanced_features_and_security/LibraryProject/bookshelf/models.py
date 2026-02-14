from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

class GeeksModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class CustomerUserModel(AbstractUser):
    date_of_birth = models.models.DateField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.username
    

class UserManager(BaseUserManager):
    def create_user(self, email,password=None):
        pass

    def create_super_user(self, email, password=None):
        pass
        