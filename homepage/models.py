from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.BigInit(primary_key=True)
    username = models.CharField(max_length = 70)
    First_name = models.CharField(max_length = 70)
    Last_name = models.CharField(max_length = 70)
    profile_image = models.ImageField(default=None)
    email = models.CharField(max_length = 70)
    password = models.CharField(max_length = 70)
    telephone = models.NumberField()
    def __str__(self):
        return self.username
