from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name= 'signup'),
    path('signin', views.signin, name= 'signin'),
    path('contact', views.contact, name= 'contact'),
    path('forgot_password', views.forgot_password, name= 'forgot_password'),
    path('set_password', views.set_password, name= 'set_password'),
    path('signout', views.signout, name= 'signout'),
    ]