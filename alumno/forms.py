from django import forms
from .models import Proyecto,Alumno
from superusuario.forms import UserForm


class MyProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'require': 'require'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'require': 'require'}),
        }

class AlumnoSelfForm(forms.ModelForm):
    NoControl = forms.CharField(label='Matricula')
    class Meta(UserForm.Meta):
        fields = '__all__'