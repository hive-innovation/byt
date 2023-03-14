from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name= 'signup'),
    path('signin', views.signin, name= 'signin'),
    path('forgot_password', views.forgot_password, name= 'forgot_password'),
    path('set_password', views.set_password, name= 'set_password'),
    path('signout', views.signout, name= 'signout'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('opensource/', views.opensource, name='opensource'),
    path('opensource/<slug:slug>/', views.open_source_detail, name='opensource-detail'),
    ]