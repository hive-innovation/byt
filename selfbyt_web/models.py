from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
class research(blog):
    def __str__(self):
        return self
class opensource(blog):
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.author
    
