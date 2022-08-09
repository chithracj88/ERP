from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class AddStudent(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length= 200)
    cgpa = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name

class AddStaff(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length= 200)
    contactno = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name
