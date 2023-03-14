from django.db import models
from django.utils.text import slugify
import uuid

class blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True) 
    category = models.CharField(max_length=1000, default='blog')
    body = models.TextField()
    slug = models.SlugField(default='default-slug', unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:300]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']


class opensource(blog):
    link = models.CharField(max_length=1000, default='link')

    def __str__(self):
        return self.link
class community_post(models.Model):
    post_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length= 200)
    like = models.IntegerField(default=0)
    Downvote = models.IntegerField(default=0)
    def __str__(self):
        self.author
    class Meta:
        ordering = ['-pub_date']

class comment(community_post):
    post_id = models.ForeignKey(on_delete=CASCADE)
    comment = models.TextField()