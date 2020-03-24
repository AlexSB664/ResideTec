from django import forms
from alumno.models import Proyecto
from .models import Oferta
from superusuario.models import User


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
                  'telefono_contacto', 'correo_contacto','carrera')
        widgets = {
            'flyer': forms.FileInput(attrs={'class': 'form-control', 'accept': 'img', 'onchange': 'loadFile(event)'}),
        }

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','password1','password2')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SimpleUserStudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
    
    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password("password")
            user.save()
        return user

class SimpleAlumnoForm(SimpleUserStudentForm):
    NoControl = forms.CharField(label='Matricula:')
    class Meta(SimpleUserStudentForm.Meta):
        model = User
        fields = ('email',)
