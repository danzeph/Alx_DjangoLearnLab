from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def user_created(sender,instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance, defaults={'role':'Member'})
        print("Your profile has successfuly been created")
