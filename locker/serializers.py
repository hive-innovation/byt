from dataclasses import fields
from pyexpat import model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import  bookshelf, courses, todo
 #creating a serializer for recieving course content
class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookshelf
        fields = [
            'book_id',
            'book_title',
            'book_description',
            'book_doc'
            ]
#  creating a serializer for recieving course content
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = [
            'course_id',
            'course_title',
            'course_description',
            'course_context'
            ]
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = [
            'todo_id',
            'task_description',
            'date_created',
            'due_date',
            'task_status'
            ]
