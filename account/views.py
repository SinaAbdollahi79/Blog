from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            

    return render(request, 'account/login.html' )


def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password1"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        User.objects.create(username=username, password=password , first_name=first_name, last_name=last_name, email=email)
    return render(request, 'account/signup.html' )



def logout_view(request):
    logout(request)
    return redirect('/')
            

    
