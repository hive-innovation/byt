from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

# handling login and signup plus homepage rendering
def home(request):
    pass
    return HttpResponse('home')
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        email = request.data.get('email')
        username = request.data.get('username')
        if Profile.objects.filter(email=email).exists():
            messages.info(request, "Email already rgistered")
            return HttpResponse('signup again')
        elif Profile.objects.filter(username=username).exists():
            messages.info(request, "username is taken")
            return HttpResponse('signup fail')
        elif serializer.is_valid():
            serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)


    return HttpResponse('login')
@api_view(['POST'])
def login(request):
     if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        user = Profile.objects.filter(email=email).first()
        if (user is None) or (not user.check_password(password)) :
            raise AuthenticationFailed('incorrect email or password')
        return HttpResponse( 'home')
def logout(reques):
    pass
@api_view(['PUT','DELETE'])
def update_account(request):
    pass
@api_view(['PUT'])
def update_password(request):
    pass
    
