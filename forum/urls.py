from urllib.request import url2pathname
from  django.urls import path
from . import views
urlpatterns = [
    path('', views.Postview, name='post'),
]