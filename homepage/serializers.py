from dataclasses import fields
from pyexpat import model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import  Profile
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
 #creating a serializer for recieving user data
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
    #creating a password hash(encrypt)
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
#used during email verification
class VerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)
    class Meta:
        model = Profile
        fields = ['token']
#sending a url during password change
class update_passwordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']

#change password 
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=8, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']
    # def validate(self, attrs):
    # # try:
    #     password = attrs.get('password')
    #     token = attrs.get('token')
    #     uidb64 = attrs.get('uidb64')
    #     id = force_str(urlsafe_base64_decode(uidb64))
    #     user = Profi.objects.get(id=id)
    #     if not PasswordResetTokenGenerator().check_token(user, token):
    #         raise AuthenticationFailed('The reset link is invalid', 401)
    #     user.set_password(password)
    #     user.save()
    #     return (user)
    # except Exception as e:
    #     raise AuthenticationFailed('The reset link is invalid', 401)
    # return super().validate(attrs)



