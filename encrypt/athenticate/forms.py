from django import forms
from django.forms import ModelForm
from .models import RegistrationModel

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields= '__all__'
        widgets={
            'password': forms.PasswordInput(),
        }