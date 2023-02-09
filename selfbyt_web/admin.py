from django.contrib import admin
from .models import blog, research, opensource
# Register your models here.
admin.site.register(blog)
admin.site.register(research)
admin.site.register(opensource)