from dataclasses import fields
from django import forms
from .models import *

class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields ='__all__' #menciono que todos los campos se van a ingresar