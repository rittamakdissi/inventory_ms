from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    adress=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(default='avatar.jpg',upload_to='profile_images')
    def __str__(self):
        return f'{self.staff.username} \'s profile'
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(staff=kwargs['instance'])
post_save.connect(create_profile,User)          
