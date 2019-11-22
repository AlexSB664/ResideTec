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
	url(r'^proyectoViejo$',views.addProjectoToLog,name="addOldProject"),
	url(r'^proyectos/index$',views.indexProjects,name="projects.index"),
	url(r'^logout$',views.logout, name='logout'),
	url(r'^ofertas/nueva$',views.nuevaOferta, name='nuevaOferta'),
]