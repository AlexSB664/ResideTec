from django import forms
from .models import Proyecto


class MyProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'require': 'require'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'require': 'require'}),
        }
