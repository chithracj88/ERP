from django import forms
from django.forms import ModelForm
from .models import AddStudent,AddStaff

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields=['name','course','cgpa']


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = AddStaff
        fields=['name','course','contactno']
        
