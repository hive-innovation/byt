from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import bookshelf, courses, todo
from .serializers import BookshelfSerializer,CourseSerializer,TodoSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# @api_view(['POST','GET'])
# def bookshelfview(request):
#     if request.method == 'POST':
#         serializer = BookshelfSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( "success", status= status.HTTP_201_CREATED)
#     if request.method == 'GET':
#         pass
@api_view(['POST', 'GET', 'DELETE'])
@parser_classes(['FileUploadParser'])
def Courseview(request, filename, format = None):
    file = request.data.get('file')
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        courses = courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        course = get_object_or_404(courses, filename=filename)
        course.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status': 'unsupported method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def todoview(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        todo_list = todo.objects.all()
        serializer = TodoSerializer(todo_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
