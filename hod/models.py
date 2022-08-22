from django.db import models
from student.models import StudentProfile
from staff.models import StaffProfile
from django.contrib.auth import get_user_model
USER = get_user_model()
# Create your models here.

class SessionYearModel(models.Model):
    start = models.DateField()
    end = models.DateField()
    year= models.CharField(max_length=120)

    def __str__(self):
        return f"{self.start} {self.end}"

class Department(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    profile = models.OneToOneField(
        StaffProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}"

class Student(models.Model):
    profile = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}"
        
class Enroll(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    session_year = models.ForeignKey(
        SessionYearModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"

    