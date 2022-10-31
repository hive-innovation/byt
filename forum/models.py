from distutils.command.upload import upload
from django.db import models
from homepage.models import Profile
import datetime

# Create your models here.
class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.CharField(max_length= 258, blank=False)
    date_created = models.DateTimeField(default= datetime.datetime.utcnow)
    post_image = models.ImageField(upload_to = 'post_images', blank=True)
    reply = models.CharField(max_length= 258, blank=False)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    shares = models.IntegerField()
    def __str__(self):
        return self.post_id

