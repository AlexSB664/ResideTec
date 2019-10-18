from django import forms
from alumno.models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','descripcion','periodo','estatus')