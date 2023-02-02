from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def logout(request):
    return redirect(request, 'home.html')
def opensource(request):
    return render(request, 'opensource.html')
def research(request):
    return render(request, 'research.html')
