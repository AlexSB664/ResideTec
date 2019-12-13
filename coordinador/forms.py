from django import forms
from alumno.models import Proyecto
from .models import Oferta


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion', 'periodo', 'estatus', 'terminado')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'require': 'require'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'require': 'require'}),
            'periodo': forms.Select(attrs={'class': 'form-control', 'require': 'require'}),
            'estatus': forms.TextInput(attrs={'class': 'form-control', 'require': 'require'}),
            'terminado': forms.CheckboxInput(attrs={'class': 'form-control', 'require': 'require'}),
        }
        labels = {
            'terminado': 'Ya fue terminado?',
        }


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ('flyer', 'titulo', 'descripcion',
                  'telefono_contacto', 'correo_contacto')
        widgets = {
            'flyer': forms.FileInput(attrs={'class': 'form-control', 'accept': 'img', 'onchange': 'loadFile(event)'}),
        }