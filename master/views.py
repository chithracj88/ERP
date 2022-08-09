from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def HomeView(request):
    context={}
    return render (request,'master/home.html',context)

def AboutView(request):
    context={}
    return render (request,'master/contact.html',context)

def LoginView(request):
    context={}
    return render (request,'master/login.html',context)

def LogoutView(request):
    context={}
    return render (request,'master/logout.html',context)

def RegistrationView(request):
    context={}
    return render (request,'master/registration.html',context)






