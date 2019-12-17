from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Proyecto, Alumno
from .forms import MyProyectoForm
from superusuario.models import Carrera, User
from coordinador.models import Oferta
# Create your views here.


@login_required
@permission_required('alumno.is_student', raise_exception=True)
def nuevoProyecto(request):
    if request.method == 'POST':
        form = MyProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.carrera = Carrera.objects.get(id=request.user.carrera.id)
            proyecto.terminado = 0
            proyecto.estatus = 'nuevo'
            proyecto.creado_por = request.user
            proyecto.save()
            if proyecto.pk is not None:
                alumno_tmp = Alumno.objects.get(email=request.user.id)
                alumno_tmp.proyecto_id = proyecto.pk
                alumno_tmp.save()
                return redirect('alumno.proyecto.detalles')
            else:
                return redirect('general.index')
    else:
        form = MyProyectoForm()
        return render(request, 'alumno/proyectos/nuevo.html', {'form': form})


@login_required
@permission_required('alumno.is_student', raise_exception=True)
def index(request):
    return render(request, 'alumno/index.html')


@login_required
@permission_required('alumno.is_student', raise_exception=True)
def mi_proyecto(request):
    alumno_tmp = Alumno.objects.get(email=request.user.id)
    if alumno_tmp.proyecto_id is None:
        return redirect('alumno.proyecto.nuevo')
    proyecto_tmp = Proyecto.objects.get(id=alumno_tmp.proyecto_id)
    return render(request, 'alumno/proyectos/detalles.html', {'proyecto': proyecto_tmp})


@login_required
@permission_required('alumno.is_student', raise_exception=True)
def editar_proyecto(request):
    alumno_tmp = Alumno.objects.get(email=request.user.id)
    proyecto_tmp = Proyecto.objects.get(id=alumno_tmp.proyecto_id)
    if request.method == 'POST':
        proyecto = MyProyectoForm(request.POST, instance=proyecto_tmp)
        proyecto.save()
        return redirect('alumno.proyecto.detalles')
    form = MyProyectoForm(instance=proyecto_tmp)
    return render(request, 'alumno/proyectos/nuevo.html', {'form': form})

@login_required
@permission_required('alumno.is_student', raise_exception=True)
def ver_ofertas(request):
    ofertas = Oferta.objects.all().filter(carrera=request.user.carrera.id).order_by('id').reverse()
    return render(request, 'coordinador/ofertas/index.html', {'ofertas': ofertas})