from distutils.command.upload import upload
from django.db import models

# creating a database for scripts(books), course
class bookshelf(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=288, null = False)
    book_description= models.CharField(max_length= 1000, blank = True, null=True )
    book_doc = models.FileField(upload_to = "scripts")
    def __str__(self) :
        return self.book_title
class courses(bookshelf):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length = 500)
    course_description = models.CharField(max_length = 1000, blank=True,null=True)
    course_context = models.FileField(upload_to = "scripts")
    def __str__(self):
        return self.course_title
