from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json 
#enables a user to create a post and 
@api_view(['POST','GET','PUT', 'DELETE'])
def Postview(request):
    if request.method == 'POST':
        serializer =PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)
    if request.method == 'GET':
        if request.method == 'GET':
            latest_posts = post.objects.filter()
            context={
                'posts': latest_posts
                }
            return Response( "ok", status= status.HTTP_200_OK)   
