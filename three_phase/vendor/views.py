from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def vendor_reg(request):
    if request.method == 'POST':
        form = CreateVendor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_login') 
    else:
        form = CreateVendor()
    context = {'form' : form }
    return render(request,'vendor_register.html',context)
    

def vendor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check if the user is a client (optional, if using groups)
            if user.groups.filter(name='Vendor').exists():
                login(request, user)
                return redirect('vendor_welcome')  # Redirect to client dashboard
            else:
                # User authenticated but not a client (informational message)
                return render(request, 'vendor_login.html', {'error_message': 'Invalid username or password.'})
        else:
            # Invalid credentials (error message)
            return render(request, 'vendor_login.html', {'error_message': 'Invalid username or password.'})
    else:
        # GET request, render login form
        return render(request, 'vendor_login.html')




def vendor_logout(request):
    logout(request)
    return redirect('vendor_login') 


@login_required
def vendor_welcome(request):
    username = request.user.username
    return render(request, 'vendor_welcome.html', {'username': username})