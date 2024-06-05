from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
                return redirect('login')
            else:
                print(form.errors)
            
        context = {'form': form}
        return render(request, 'login/register.html', context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
            
        context = {}
        return render(request, 'login/login.html', context)

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'login/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')