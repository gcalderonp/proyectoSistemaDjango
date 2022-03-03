from django.db.models import fields
from django import forms
from .models import libro

class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = "__all__" #menciono que todos los campos se van a ingresar
        Widget = {
            'tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estadi Civil'
                }
            )
        }