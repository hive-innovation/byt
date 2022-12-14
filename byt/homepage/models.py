from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 70)
    First_name = models.CharField(max_length = 70)
    Last_name = models.CharField(max_length = 70)
    profile_image = models.ImageField(default=None, uplooad_to = 'media')
    email = models.CharField(max_length = 70)
    password = models.CharField(max_length = 70)
    telephone = models.IntegerField()
    def __str__(self):
        return self.username
