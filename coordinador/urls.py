from django.conf.urls import *
from coordinador import views

urlpatterns = [
	url(r'^$',views.login, name='index'),
	url(r'^login$',views.login, name='login'),
	url(r'^index$',views.generalIndex, name='general.index'),
	url('register',views.register, name='register'),
    url(r'^index$',views.index, name='Welcome'),
	url('calificaciones',views.calificaciones,name="calificaciones"),
	url('ofertaproyecto',views.offerproyecto,name="offerproy"),
	url('ofertainvestigacion',views.offerinvestiga,name="offerinv"),
	url(r'^coordinador/proyectoViejo$',views.addProjectoToLog,name="coor.addOldProject"),
	url(r'^coordinador/proyectos/index$',views.indexProjects,name="coor.projects.index"),
	url(r'^logout$',views.logout, name='logout'),
	url(r'^coordinador/ofertas/nueva$',views.nuevaOferta, name='coor.nuevaOferta'),
	url(r'^coordinador/ofertas/index$',views.indexOferta, name='coor.ofertas.index'),
	url(r'^coordinador/usuarios/perfil$',views.perfilPublico, name='perfil.publico'),
	url(r'^coordinador/ofertas/detalles$',views.detalleOferta, name='detalleoferta'),
	url(r'^coordinador/alumnos/nuevos$',views.nuevoAlumno, name='coor.alumno.nuevo'),
	url(r'^coordinador/alumnos/index$',views.indexAlumno, name='coor.alumno.index'),
]
