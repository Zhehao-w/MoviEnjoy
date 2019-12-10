from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class UserProfileInfo(models.Model):
    # to add more attributes to the built-in user table
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # addition fields
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(auto_now=False,auto_now_add=False,unique=False)
    occupation = models.CharField(max_length=254,unique=False)
    introduction = models.TextField(blank=True)
    profile_pic = models.ImageField(default='Default.jpg',upload_to='profile_pics', blank=True)
    register_date = models.DateField(auto_now_add=True,unique=False)

    def __str__(self):
        return f'{self.user.username} Profile'
