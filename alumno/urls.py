from django.conf.urls import *
from alumno import views

urlpatterns = [
	url(r'^alumnos/proyectos/nuevo$',views.nuevoProyecto, name='alumno.proyecto.nuevo'),
	url(r'^alumnos/index$',views.index, name='alumno.index'),
]