from django.shortcuts import render
from locker.models import courses
from urllib import request
from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from .models import search_query
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from locker.models import courses
from forum.models import post
import json
from .serializers import SearchSerializer
from django.db.models import Q

@api_view(['POST'])
def search(request):
    if request.method == "POST":
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data.get('search_query')
            multi_search = Q(Q(course_title__icontains=data) | Q(course_description__icontains=data))
            search_result = courses.objects.filter(multi_search)
            serialized_result = SearchSerializer(search_result, many=True)
            return Response(serialized_result.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
