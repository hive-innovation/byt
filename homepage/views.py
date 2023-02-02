from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt, datetime, utils 
from  django.core.mail import *
from .serializers import VerifySerializer, update_passwordSerializer, SetNewPasswordSerializer
from .models import Profile
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token


# handling login and signup plus homepage rendering
def home(request):
    pass
    return HttpResponse('home.html')
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        email = request.data.get('email')
        username = request.data.get('username')
        if Profile.objects.filter(email=email).exists():
            messages.info(request, "Email already registered")
            return Response({"error": "Email already registered"}, status=400)
        elif Profile.objects.filter(username=username).exists():
            messages.info(request, "Username is taken")
            return Response({"error": "Username is taken"}, status=400)
        else:
            if serializer.is_valid():
                user = serializer.save()
                # current_site = get_current_site(request)
                subject = 'Activate Your Account'
                message = render_to_string('user/verification_email.html', {
                    'user': user,
                    'domain': 'fmbishu@gmail.com',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMultiAlternatives(
                    subject, message, to=[to_email]
                )
                email.attach_alternative(message, "text/html")
                email.send()
                messages.success(request, 'Please confirm your email address to complete the registration.')
                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=400)
@api_view(['POST'])
def verify_email(request):
    serializer = VerifySerializer(data=request.data)
    if serializer.is_valid():
        profile = Profile.objects.get(user=request.user)
        profile.email_confirmed = True
        profile.save()
        return Response({"message": "Email verified successfully"})
    return Response(serializer.errors, status=400)
@api_view(['POST'])
def login(request):
     if request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        password = request.data.get('password')
        email = request.data.get('email')
        user = Profile.objects.filter(email=email).first()
        if user is None:
                raise AuthenticationFailed('email wrong')
        if not user.check_password(password):
            raise AuthenticationFailed('wrong password')
        # generates a token for a user once credentials are verified. with an creation time(iat) and an expiration time (exp)
        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=180),
            'iat': datetime.datetime.utcnow()
        }
        #this is built simply just for beta version. will be  updated with OAuth2.0 
        token = jwt.encode(payload,key='secret',algorithm="HS256").decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token,httponly=True )
        return Response( "ok", status= status.HTTP_200_OK)
@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    return Response( "ok", status= status.HTTP_200_OK)

import json
# @api_view(['PUT','DELETE'])
# def update_account(request, id):
#     try:
#         profile = Profile.objects.get(pk=id)
#     except:
#         return Response("not found", status= status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     if request.method == 'DELETE':
#         profile.delete()
#         return Response("deleted", status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_password(request,id):
    try:
        profile = Profile.objects.get(pk=id)
    except:
        return Response("not found", status= status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def send_password_reset_email(request):
    serializer = update_passwordSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return Response({"error": "This email address is not registered with us."}, status=400)
        # current_site = get_current_site(request)
        # site_name = current_site.name
        # domain = current_site.domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        context = {
            # 'domain': domain,
            # 'site_name': site_name,
            'uid': uid,
            'token': token,
            'protocol': 'https' if request.is_secure() else 'http',
        }
        subject = loader.render_to_string('user/reset_password_subject.txt', context)
        message = loader.render_to_string('user/reset_password_email.html', context)
        send_mail(subject, message, 'fmbishu@gmail.com', [email], fail_silently=False)
        return Response({"message": "Password reset email sent successfully"})
    return Response(serializer.errors, status=400)
@api_view(['POST'])
def set_new_password(request):
    serializer = SetNewPasswordSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data['password']
        token = serializer.validated_data['token']
        uidb64 = serializer.validated_data['uidb64']
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Profile.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            return Response({"message": "Password set successfully"})
        else:
            return Response({"error": "Invalid/Expired token"}, status=400)
    return Response(serializer.errors, status=400)