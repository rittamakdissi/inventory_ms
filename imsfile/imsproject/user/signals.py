'''from django.contrib.auth.decorators import User
from .models import Profile 
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile (sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(staff=instance,name=instance.username)

@receiver(post_save,sender=User)
def save_profile (sender,instance,**kwargs):
    instance.Profile.save()       '''