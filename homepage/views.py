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
import jwt, datetime


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
@api_view(['POST'])
def login(request):
     if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        password = request.data.get('password')
        email = request.data.get('email')
        user = Profile.objects.filter(email=email).first()
        if user is None:
                raise AuthenticationFailed('email wrong')
        if not user.check_password(password):
            raise AuthenticationFailed('wrong password')
        # generates a token for a user once credentials are verified. with an creation time(iat) and an expiration time (exp)
        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=180),
            'iat': datetime.datetime.utcnow()
        }
        #this is built simply just for beta version. will be  updated with OAuth2.0 
        token = jwt.encode(payload,key='secret',algorithm="HS256").decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token,httponly=True )
        return Response( "ok", status= status.HTTP_200_OK)
@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    return Response( "ok", status= status.HTTP_200_OK)

import json
@api_view(['PUT','DELETE'])
def update_account(request, id):
    try:
        profile = Profile.objects.get(pk=id)
    except:
        return Response("not found", status= status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        profile.delete()
        return Response("deleted", status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_password(request,id):
    try:
        profile = Profile.objects.get(pk=id)
    except:
        return Response("not found", status= status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)
    
