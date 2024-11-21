from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserProfile

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        number = request.POST['number']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('sign_up')

        # Create User and UserProfile
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        UserProfile.objects.create(user=user, address=address, number=number)

        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('sign_in')
    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in and redirect to the home page
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home-page')  
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password')
            return redirect('sign_in')  

    return render(request, 'sign_in.html')

def master(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())
    
def home_page(request):
    
    return render(request, 'home-page.html')

def cat_tree(request):
    return render(request, 'cat_tree.html')

def cart(request):
    return render(request, 'cart.html')