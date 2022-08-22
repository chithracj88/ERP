from django import forms
from django .forms import ModelForm
from .models import StudentProfile

class StudentProfileForm(ModelForm):
    class Meta:
        model=StudentProfile
        exclude = [
            "status",
            "created_on",
            "updated_on",
        ]

       
		
    

    