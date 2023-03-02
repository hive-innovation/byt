from django.urls import path, re_path
from . import views
#from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
urlpatterns=[
    path('register', views.register, name = 'register'), 
    path('login', views.login, name = 'login'),
    path('logout', views.login, name = 'logout'),
    path('password_reset', views.send_password_reset_email, name = 'send_password_reset_email'),
    path('set_new_password/', views.set_new_password, name = 'set_new_password'),
    # path('update_account/<int:id>', views.update_account, name = 'update_account'),
    path('verify_email/', views.verify_email, name='verify_email')
]