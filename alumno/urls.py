from django.conf.urls import *
from alumno import views

urlpatterns = [
	url(r'^alumnos/proyectos/nuevo$',views.nuevoProyecto, name='alumno.proyecto.nuevo'),
	url(r'^alumnos/proyectos/detalles$',views.mi_proyecto, name='alumno.proyecto.detalles'),
	url(r'^alumnos/proyectos/editar$',views.editar_proyecto, name='alumno.proyecto.editar'),	
	url(r'^alumnos/index$',views.index, name='alumno.index'),
]