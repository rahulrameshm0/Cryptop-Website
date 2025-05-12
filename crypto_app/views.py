from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about_layout.html')

def how(request):
    return render(request, 'how_layout.html')
    
def login_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, name=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull')

        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'login.html')

def signup_account(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['password']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email address already exists')
            return redirect('register')
        
        create_user = User.objects.create_user(username=username, password=password, email=email, confirm_password=confirm_password)
        create_user.save()

        messages.success(request, 'You have registerd succesfully!')
        return redirect('login')