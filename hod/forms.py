from dataclasses import fields
from xml.etree.ElementInclude import include
from django import forms
from django .forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","email"]

class SessionYearForm(forms.ModelForm):
    class Meta:
        model=SessionYearModel
        fields='__all__'

class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = [
            "status",
            "created_on",
            "updated_on",
        ]

class AddCourseForm(ModelForm):
	class Meta:
		model=Course
		exclude = [
            "status",
            "created_at",
            "updated_at",
        ]

class StaffForm(ModelForm):
	class Meta:
		model=Staff
		fields = [
            'user',
            'department',
            'course',
        ]
        
class StudentForm(ModelForm):
	class Meta:
		model=Student
		fields = [
            'user',            
        ]
        
class EnrollForm(ModelForm):
    class Meta:
        model=Enroll
        exclude = [
            "status",
            "created_at",
            "updated_at",
        ]