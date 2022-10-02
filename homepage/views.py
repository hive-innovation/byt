from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
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
        if Profile.objects.filter(email=email).first():
            messages.info(request, "Email already rgistered")
            return HttpResponse('signup again')
        elif Profile.objects.filter(username=username).first():
            messages.info(request, "username is taken")
            return HttpResponse('signup fail')
        else:
            if serializer.is_valid():
                serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)


        return HttpResponse('login')
@api_view(['POST'])
def login(request):
     if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        password = request.data.get('password')
        email = request.data.get('email')
        user = Profile.objects.filter(email=email).first()
        userpass = Profile.objects.filter(password=password)
        if user is None:
                raise AuthenticationFailed('email wrong')
        if not user.check_password(password):
            raise AuthenticationFailed('wrong password')

        return HttpResponse( 'home'+ password)
        #{"username":"sdfghj","first_name":"wertyui","last_name":"xcvbnm","email":"fghjhgf@rtt.com","password":"abcdefg"}
        #pbkdf2_sha256$390000$wU0ci8r1V1sZqTw06f6Du1$1fwh2rTZX7D+qYW1ouQZ2BSKv8pWzCLmI6T596lIpWs=
       # pbkdf2_sha256$390000$GVn4685Q8VzJ99UUfUrHg8$j96YdEs7qYXblmYuOvDGnul2y8BoV2m+JDRBv6wDdR4= 
def logout(request):
    pass
@api_view(['PUT','DELETE'])
def update_account(request):
    pass
@api_view(['PUT'])
def update_password(request):
    pass
    
