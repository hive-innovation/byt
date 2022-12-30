from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
urlpatterns=[
    path('signup', views.signup, name = 'signup'), 
    path('login', views.login, name = 'login'),
    path('logout', views.login, name = 'logout'),
    path('update_account/<int:id>', views.update_account, name = 'update_account')
]