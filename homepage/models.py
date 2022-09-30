from enum import unique
from django.db import models
# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 70)
    First_name = models.CharField(max_length = 70)
    Last_name = models.CharField(max_length = 70)
    profile_image = models.ImageField(upload_to = 'media', default = None)
    email = models.CharField(max_length = 70, unique = True)
    password = models.CharField(max_length = 70)
    telephone = models.IntegerField()
    def __str__(self):
        return self.username
