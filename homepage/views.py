from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# handling login and signup plus homepage rendering
def home(request):
    pass
    return HttpResponse('home')
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data = rquest.data)
        email = request.data.get('email')
        username = request.data.get('username')
        if profile.objects.filter(email=email).exist():
            messages.info(request, "Email already rgistered")
            return HttpResponse('signup again')
        elif profile.objects.filter(username=username).exist():
            messages.info(request, "username is taken")
            return HttpResponse('signup fail')
        else:
            serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)


    return HttpResponse('login')
@api_view(['POST'])
def login(request):
     if request.method == 'POST':
        serializer = ProfileSerializer(data = rquest.data)
        return HttpResponse( 'home')
    
