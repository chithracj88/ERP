from django.shortcuts import render

# Create your views here.

def HomeView(request):
    context={}
    return render (request,'master/home.html',context)

def AboutView(request):
    context={}
    return render (request,'master/aboutus.html',context)

def LoginView(request):
    context={}
    return render (request,'master/login.html',context)

def LogoutView(request):
    context={}
    return render (request,'master/logout.html',context)






