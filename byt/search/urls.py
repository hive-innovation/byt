from  django.urls import path
from . import views
#link to search screen
urlpatterns = [
    path('search', views.search_screen, name='search')
]