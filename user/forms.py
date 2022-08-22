from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class StudentRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","email"]


