from django.shortcuts import render, redirect
from .forms import StudentProfileForm

def student_home(request):
    return render(request,"student/home_content.html")

def student_profile(request):
    submitted= False
    if request.method == 'POST':
        form=StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"student/student_profile.html")

    else:
            form=StudentProfileForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "student/student_profile.html",{'form':form,'submitted':submitted})
    
    
    
    