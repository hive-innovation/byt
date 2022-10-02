from enum import unique
from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(max_length = 70, unique=True )
    profile_image = models.ImageField(upload_to = 'media', default = None)
    email = models.CharField(max_length = 70, unique = True)
    password = models.CharField(max_length = 70)
    def __str__(self):
        return self.email
