from dataclasses import fields
from .models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()

class Easy(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email")
        field_classes = {"username":UsernameField}
        
class Img(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ("logo",)