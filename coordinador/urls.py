from django.conf.urls import *
from coordinador import views

urlpatterns = [
	url(r'^$',views.login, name='index'),
	url(r'^login$',views.login, name='login'),
	url('register',views.register, name='register'),
    url('index',views.index, name='Welcome'),
	url('calificaciones',views.calificaciones,name="calificaciones"),
	url('ofertaproyecto',views.offerproyecto,name="offerproy"),
	url('ofertainvestigacion',views.offerinvestiga,name="offerinv"),
	url(r'^historyResidencie.php$',views.history,name="addToHistory"),
]