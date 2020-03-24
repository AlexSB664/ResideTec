from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'nombre_usuario', 'nombres', 'apellido_paterno', 'apellido_materno',
                  'fecha_nacimiento', 'direccion', 'telefono', 'genero', 'foto_perfil')
        widgets = {
            'flyer': forms.FileInput(attrs={'class': 'form-control', 'accept': 'img', 'onchange': 'loadFile(event)'}),
        }
