from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import StudentRegisterForm
#password rest

def HomeView(request):
    return render (request,'home.html',{})


class LoginPage(View):
    def get(self,request):
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'login.html',context)

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            if user.is_superuser == True and user.is_staff == True:
                return redirect('hod/admin_home')
            if user.is_superuser == False and user.is_staff == True:
                return redirect('staff/staff_home')
            if user.is_superuser == False and user.is_staff == False:
                return redirect('student/student_home')
        else:
            form=AuthenticationForm()
            context={'form':form}
            return render(request,'login.html',context)
    
def Logout(request):
    return render (request,'login.html',{})

class RegisterStudent(View): 

    template_name='register.html' 
    def get(self,request): 
        context={'form':StudentRegisterForm} 
        return render(request,self.template_name,context) 
    def post(self,request): 
        username=request.POST.get('username') 
        password=request.POST.get('password1') 
        email=request.POST.get('email') 
        first_name=request.POST.get('first_name') 
        last_name=request.POST.get('last_name') 
        user=User.objects.create(username=username,
            password=password, 
            email=email, 
            first_name=first_name,
            last_name=last_name,
            is_staff=False)
        user.set_password(password)
        user.save()
        return render(request,'register.html',{})






    

     
    