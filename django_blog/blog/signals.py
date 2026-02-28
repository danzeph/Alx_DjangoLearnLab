from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import UserProfile

@receiver(post_save, sender=User)
def user_created(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        print("User profile created sucessfully")

    else:
        try:
            instance.userprofile.save()
            print("User profile updated sucessfully")
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
