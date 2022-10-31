from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import  search_query
 #creating a serializer for recieving user data
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = search_query
        fields = [
            'search_query',
            'date_of_query'
            ]