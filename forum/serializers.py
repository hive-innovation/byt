from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import  post
 #creating a serializer for recieving posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = [
            'post_id',
            'created_by',
            'post',
            'date_created',
            'post_image',
            'reply',
            'likes',
            'dislikes',
            'shares'
            ]