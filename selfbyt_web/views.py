from django.shortcuts import render, redirect
from  django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt, datetime, utils 
from  django.core.mail import *
from homepage.serializers import VerifySerializer, update_passwordSerializer, SetNewPasswordSerializer, ProfileSerializer
from homepage.models import Profile
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
from homepage.tokens import account_activation_token
from .models import blog, opensource, research

# Create your views here.
def home(request):
    return render(request, 'home.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def signup(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.POST)
        email = request.POST['email']
        username = request.POST['username']
        if Profile.objects.filter(email=email).exists():
            messages.info(request, "Email already registered")
        elif Profile.objects.filter(username=username).exists():
            messages.info(request, "Username is taken")
        else:
            if serializer.is_valid():
                user = serializer.save()
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
                messages.info(request, 'Please confirm your email address to complete the registration.')
                return redirect(request, 'user/login.html')
    return render(request, 'user/signup.html')
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = Profile.objects.filter(email=email).first()
        if user is None:
            messages.info(request, 'Email not found')
            return render(request, 'user/login.html')
        password = request.POST['password']
        if not user.check_password(password):
            messages.info(request, 'Wrong password')
            return render(request, 'user/login.html')
        # generates a token for a user once credentials are verified. with a creation time(iat) and an expiration time (exp)
        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=180),
            'iat': datetime.datetime.utcnow()
        }
        #this is built simply just for beta version. will be updated with OAuth2.0 
        token = jwt.encode(payload,key='secret',algorithm="HS256")
        response = Response()
        response.set_cookie(key='jwt', value=token,httponly=True )
        return redirect('home')
    return render(request, 'user/login.html')
def signout(request):
    response = Response()
    response.delete_cookie('jwt')
    return redirect(request, 'home.html')
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            messages.info(request,"enter a valid email")
            return render(request, 'user/forgot_password.html')
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
        messages.info(request, 'An email has been sent to your email address.')
        return render(request, 'user/forgot_password.html')
    return render(request, 'user/forgot_password.html')
def set_password(request):
    serializer = SetNewPasswordSerializer(data=request.POST)
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
            messages.info(request,"Password set successfully")
            return render('user/login.html')
        else:
            messages.info(request,  "Invalid/Expired token")
    return render(request, 'user/set_new_password.html')
def opensource_page(request):
    return render(request, 'opensource.html')
def research_page(request):
    return render(request, 'research.html')
