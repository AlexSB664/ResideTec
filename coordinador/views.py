from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from .forms import ProyectoForm,OfertaForm
from alumno.models import Proyecto
from .models import Oferta
from superusuario.models import User
# Create your views here.
import sys
from pprint import pprint


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

@login_required
def indexProjects(request):
    projects = Proyecto.objects.all()
    return render(request,'coordinador/projectsIndex.html',{'projects':projects})

@login_required
def nuevaOferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.flyer = request.FILES['flyer']
            oferta.creado_por = User.objects.get(id=request.user.id)
            if oferta.save():
                return redirect('ofertas.index')
            else:
                return redirect('ofertas.index')
    else:
        form = OfertaForm()
        return render(request,'coordinador/ofertas/nueva.html',{
            'form':form
        })

@login_required
def indexOferta(request):
    ofertas = Oferta.objects.order_by('id').reverse()
    return render(request,'coordinador/ofertas/index.html',{'ofertas':ofertas})

@login_required
def perfilPublico(request):
    user = User.objects.get(id=request.GET['userid'])
    return render(request,'coordinador/perfil/view.html',{'coruser':user})

@login_required
def detalleOferta(request):
    offer = Oferta.objects.get(id=request.GET['offerid'])
    return render(request, 'coordinador/ofertas/detail.html',{'oferta':offer})