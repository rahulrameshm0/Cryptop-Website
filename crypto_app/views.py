from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about_layout.html')

def how(request):
    return render(request, 'how_layout.html')
    
def login_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfull')
            return render(request, 'index.html')

        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists!')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email address already exists!')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Passowrd does not match')
            return redirect('register')
        
        create_user = User.objects.create_user(username=username, password=password, email=email)
        create_user.save()

        messages.success(request, 'You have registerd succesfully!')
        return redirect('login')
    
    return render(request, 'register.html')

