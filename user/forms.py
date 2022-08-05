from django import forms
from django.forms import ModelForm
from .models import Location,Address,Profile,SessionYearModel,Department,Course,Staff,Student,Enroll

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class Address(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

class Profile(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class SessionYearModel(ModelForm):
    class Meta:
        model = SessionYearModel
        fields = "__all__"

class Department(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class Course(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class Staff(ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class Student(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class Enroll(ModelForm):
    class Meta:
        model = Enroll
        fields = "__all__"



