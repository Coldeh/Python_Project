from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import *
# Create your views here.
def clientreg(request):
    if request.method == 'POST':
        form = CreateClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_login') 
    else:
        form = CreateClient()
    context = {'form' : form }
    return render(request,'clientregister.html',context)
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check if the user is a client (optional, if using groups)
            if user.groups.filter(name='Client').exists():
                login(request, user)
                return redirect('client_dashboard')  # Redirect to client dashboard
            else:
                # User authenticated but not a client (informational message)
                return render(request, 'client_login.html', {'error_message': 'You are not authorized to access the client dashboard.'})
        else:
            # Invalid credentials (error message)
            return render(request, 'client_login.html', {'error_message': 'Invalid username or password.'})
    else:
        # GET request, render login form
        return render(request, 'client_login.html')

def client_logout(request):
    logout(request)
    return redirect('client_login') 


@login_required
def welcome(request):
    username = request.user.username
    return render(request, 'welcome.html', {'username': username})
