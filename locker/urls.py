from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
urlpatterns=[
    path('bookshelf', views.bookshelfview, name = 'bookshelf'), 
    path('course', views.Courseview, name = 'courses'),
    path('todo', views.todoview, name = 'todo')
]