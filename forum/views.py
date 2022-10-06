from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST','GET'])
def Postview(request):
    if request.method == 'POST':
        serializer =PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "book addded", status= status.HTTP_201_CREATED)
    if request.method == 'GET':
        pass
