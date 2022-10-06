from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import bookshelf, courses, todo
from .serializers import BookshelfSerializer,CourseSerializer,TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST','GET'])
def bookshelfview(request):
    if request.method == 'POST':
        serializer = BookshelfSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "book addded", status= status.HTTP_201_CREATED)
    if request.method == 'GET':
        pass
@api_view(['POST','GET'])
def Courseview(request):
     if request.method == 'POST':
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "course addded", status= status.HTTP_201_CREATED)
     if request.method == 'GET':
         pass
@api_view(['POST','GET'])
def todoview(request):
     if request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "task added", status= status.HTTP_201_CREATED)
     if request.method == 'GET':
         pass