from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto,Alumno
from .forms import MyProyectoForm
from superusuario.models import Carrera,User
# Create your views here.

@login_required
def nuevoProyecto(request):
    if request.method == 'POST':
        form = MyProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.carrera = Carrera.objects.get(id=request.user.carrera.id)
            proyecto.terminado = 0
            proyecto.estatus = 'nuevo'
            if proyecto.save():
                alumno_tmp = Alumno.objects.get(id = request.user.id)
                alumno_tmp.proyecto_id = proyecto.id
                return redirect('general.index')
            else:
                return redirect('general.index')
    else:
        form = MyProyectoForm()
        return render(request,'alumno/proyectos/nuevo.html',{'form':form})

@login_required
def index(request):
    return render(request,'alumno/index.html')