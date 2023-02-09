from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name= 'register'),
    path('signin', views.signin, name= 'signin'),
    path('contact', views.contact, name= 'about'),
    path('signout', views.signout, name= 'signout')]