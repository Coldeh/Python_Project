
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
def admin_reg(request):
    if request.method == 'POST':
        form = CreateAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login') 
    else:
        form = CreateAdmin()
    context = {'form' : form }
    return render(request,'admin_register.html',context)


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check if the user is a client (optional, if using groups)
            if user.groups.filter(name='Admin').exists():
                login(request, user)
                return redirect('admin_welcome')  # Redirect to client dashboard
            else:
                # User authenticated but not a client (informational message)
                return render(request, 'admin_login.html', {'error_message': 'Invalid username or password.'})
        else:
            # Invalid credentials (error message)
            return render(request, 'admin_login.html', {'error_message': 'Invalid username or password.'})
    else:
        # GET request, render login form
        return render(request, 'admin_login.html')




def admin_logout(request):
    logout(request)
    return redirect('admin_login') 


@login_required
def admin_welcome(request):
    username = request.user.username
    return render(request, 'admin_welcome.html', {'username': username})