from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
urlpatterns=[
    path('signup', views.signup, name = 'signup'), 
    path('login', views.login, name = 'login'),
    path('logout', views.login, name = 'logout'),
    path('password_reset', views.send_password_reset_email, name = 'send_password_reset_email'),
    path('set_new_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.set_new_password, name = 'set_new_password'),
    # path('update_account/<int:id>', views.update_account, name = 'update_account'),
    path('verify_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.verify_email, name='verify_email'), 
]