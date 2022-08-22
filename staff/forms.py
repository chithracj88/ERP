from django import forms
from django .forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class AddStaffLocationForm(forms.ModelForm):
    class Meta:
        model =StaffLocation
        fields = '__all__'

class StaffAddressForm(forms.ModelForm):
    class Meta:
        model =StaffAddress
        fields = '__all__'

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model =StaffProfile
        exclude = [
            "status",
            "created_on",
            "updated_on",
        ]
        