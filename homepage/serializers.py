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
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True}
        }
def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance
