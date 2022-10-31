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

#search algorithm for searching courses
@api_view(['POST'])
def search(request):
    if request.method == "POST":
        serializer = SearchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        data = request.data.get('search_query')
        multi_search = Q(Q(course_title_icontains=data) | Q(course_description_icontains=data) )
        search_result = courses.objects.filter(multi_search)
        result ={
            'data': search_result
        }
    return render(result)
"""def for_you(request):
    pass
    return render(request)
def popular(request):
    pass"""

