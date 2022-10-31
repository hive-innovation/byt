from django.contrib import admin
from  .models import bookshelf, courses, todo
# add profile table to admin site.
admin.site.register(bookshelf)
admin.site.register(courses)
admin.site.register(todo)
