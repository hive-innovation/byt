from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import  Profile
 #creating a serializer for recieving user data
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'First_name',
            'Last_name',
            'email',
            'password',
            'telephone'
            ]

