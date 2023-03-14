from django.db import models
from django.utils.text import slugify
import uuid
from django.conf import settings
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
    post_id = models.AutoField(primary_key=True)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    Downvote = models.IntegerField(default=0)
    def __str__(self):
        self.post_id
    class Meta:
        ordering = ['-pub_date']

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    parent_post = models.ForeignKey(community_post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.author
    
    class Meta:
        ordering = ['-pub_date']
