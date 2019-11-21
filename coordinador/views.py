from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from .forms import ProyectoForm
from alumno.models import Proyecto
# Create your views here.
import sys


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            if (user.has_perm('coordinador.is_admin')):
                return redirect('general.index')
            else:
                return redirect('logout')
        else:
            mensaje = "Error contraseña o correo no valido"
            return render(request, 'login.html', {'mensaje': mensaje})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request.user)
    return redirect('login')

@login_required
def generalIndex(request):
    return render(request, 'coordinador/addResidencia.html')


@login_required
def register(request):
    return render(request, 'register.html')


@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def calificaciones(request):
    return render(request, 'calificaciones.html')


@login_required
def offerproyecto(request):
    return render(request, 'ofertaproy.html')


@login_required
def offerinvestiga(request):
    return render(request, 'ofertainv.html')


@login_required
def addProjectoToLog(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            if project.save():
                return redirect('login')
            else:
                return redirect('login')
    else:
        form = ProyectoForm()
        return render(request,'coordinador/addResidencia.html',{
            'form':form
        })

def indexProjects(request):
    projects = Proyecto.objects.all()
    return render(request,'coordinador/projectsIndex.html',{'projects':projects})