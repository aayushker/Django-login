from django.shortcuts import render
# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'login/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login/login.html', context)