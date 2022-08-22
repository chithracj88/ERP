from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from hod.forms import UserRegisterForm,AddCourseForm,StaffForm,EnrollForm,SessionYearForm,StudentForm
from django.contrib.auth.models import User
from django.views import generic as views
from django.urls import reverse_lazy
from .models import *


#homeview for Hod
def admin_home(request):
    student_count=Student.objects.all().count()
    staff_count=Staff.objects.all().count()
    course_count= Course.objects.all().count()
    department_count=Department.objects.all().count()

    return render(request,"hod/home_content.html",{'student_count':student_count," staff_count": staff_count,
    "course_count":course_count,"department_count":department_count})


class SessionView(View):
        form_class = SessionYearForm
        initial = {'key': 'value'}
        template_name = 'hod/session_year.html'

        def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'hod/session_year.html')

            return render(request, self.template_name, {'form': form})

#faculty registration by HOD
class Register(View): 

    template_name='hod/register.html' 
    def get(self,request): 
        context={'form':UserRegisterForm} 
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
            is_staff=True)
        user.set_password(password)
        user.save()
        return render(request,'hod/register.html',{})
#ADD Department by HOD

def AddDepartment(request):
        if request.method == 'POST':
            if request.POST.get('name'):
                post=Department()
                post.name= request.POST.get('name')
                post.save()
                
                return render(request, 'hod/add_department.html')  

        else:
                return render(request,'hod/add_department.html')
#List all department
def All_Department(request):
    context ={}
    context["department"] = Department.objects.all()
    return render(request, 'hod/list_department.html',context)  

#Delete the department
class DepartmentDelete(views.DeleteView):
    model = Department
    template_name='hod/delete_department.html'
    success_url= reverse_lazy('hod:list_department')

#Add Course by HOD
def add_course(request):
    submitted= False
    if request.method == 'POST':
        form=AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "hod/add_course.html")

    else:
            form=AddCourseForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "hod/add_course.html",{'form':form,'submitted':submitted})
    
#LIST all the courses created und each department  
def manage_course(request):
    context ={}
    context["course"] = Course.objects.all()
    return render(request, "hod/manage_course.html",context)

#Delete course by HOD
class CourseDelete(views.DeleteView):
    model = Course
    template_name='hod/delete_course.html'
    success_url= reverse_lazy('hod:manage_course')

#Assign staff to each department and course
def assign_staff(request):
    submitted= False
    if request.method == 'POST':
        form=StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "hod/assign_staff.html")

    else:
            form=StaffForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "hod/assign_staff.html",{'form':form,'submitted':submitted})

#LIST all the staff 

def manage_staff(request):
    context ={}
    context["staff"] = Staff.objects.all()
    return render(request, "hod/manage_staff.html",context)

#Delete faculty by HOD
class StaffDelete(views.DeleteView):
    model = Staff
    template_name='hod/delete_staff.html'
    success_url= reverse_lazy('hod:manage_staff')

#update staff
class StaffUpdate(views.UpdateView):
    template_name = "hod/update_staff.html"
    model = Staff
    form_class = StaffForm
    success_url= reverse_lazy('hod:manage_staff')
#students
class StudentView(View):
        form_class = StudentForm
        initial = {'key': 'value'}
        template_name = 'hod/student.html'

        def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'hod/student.html')

            return render(request, self.template_name, {'form': form})


#Delete student by HOD
class StudentDelete(views.DeleteView):
    model = Student
    template_name='hod/delete_student.html'
    success_url= reverse_lazy('hod:manage_student')

#Update staff
class StudentUpdate(views.UpdateView):
    template_name = "hod/update_student.html"
    model = Enroll
    form_class = EnrollForm
    success_url= reverse_lazy('hod:manage_student')

#entroll students
def enroll(request):
    submitted= False
    if request.method == 'POST':
        form=EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "hod/enroll.html")

    else:
            form=EnrollForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request, "hod/enroll.html",{'form':form,'submitted':submitted})

#LIST all the student
def manage_student(request):
    context ={}
    context["enroll"] = Enroll.objects.all()
    return render(request, "hod/manage_student.html",context)
