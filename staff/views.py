from django.shortcuts import render, redirect
from .models import *
from .forms import AddStaffLocationForm,StaffAddressForm,StaffProfileForm
from django.urls import reverse_lazy 
from django.views import generic as views
from django.contrib.auth.decorators import login_required

@login_required
def staff_home(request):
    return render(request,"staff/home_content.html")

def add_stafflocation(request):

    submitted= False
    if request.method == 'POST':
        form=AddStaffLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "staff/add_stafflocation.html")

    else:
            form=AddStaffLocationForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "staff/add_stafflocation.html",{'form':form,'submitted':submitted})
    

def list_stafflocation(request):
    context ={}
    context["staffloactions"] = StaffLocation.objects.all()
    return render(request, 'staff/list_stafflocation.html',context)  

#create Staff Address
def add_staffaddress(request):
    submitted= False
    if request.method == 'POST':
        form=StaffAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "staff/add_staffaddress.html")

    else:
            form=StaffAddressForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "staff/add_staffaddress.html",{'form':form,'submitted':submitted})

#create staff profile
def add_staffprofile(request):
    submitted= False
    if request.method == 'POST':
        form=StaffProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"staff/add_staffprofile.html")
    else:
            form=StaffProfileForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request,"staff/add_staffprofile.html",{'form':form,'submitted':submitted})

 
def manage_staffprofile(request):
    context ={}
    context["profile"] = StaffProfile.objects.all()   
    return render(request, "staff/profile.html",context)

