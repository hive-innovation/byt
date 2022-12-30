from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import bookshelf, courses, todo
from .serializers import BookshelfSerializer,CourseSerializer,TodoSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST','GET'])
def bookshelfview(request):
    if request.method == 'POST':
        serializer = BookshelfSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)
    if request.method == 'GET':
        pass
@api_view(['POST','GET', 'PUT', 'DELETE'])
@parser_classes(['FileUploadParser'])
def Courseview(request, filename, format = None):
     file = request.data.get('file')
     if request.method == 'POST':
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "successs", status= status.HTTP_201_CREATED)
     if request.method == 'GET':
         pass   
@api_view(['POST','GET'])
def todoview(request):
     if request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( "success", status= status.HTTP_201_CREATED)
     if request.method == 'GET':
        todo_list = todo.objects.filter()
        context = {
            "data": todo_list
            }
        return Response("ok", status.HTTP_200_OK)
