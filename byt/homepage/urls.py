from django.urls import path
from . import views
urlpatterns=[
    path('', view = views.getstarted)
    path('useful/', view = views.useful)
]