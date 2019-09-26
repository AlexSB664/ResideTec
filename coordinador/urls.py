from django.conf.urls import *
from coordinador import views

urlpatterns = [
	url(r'^$',views.login, name='index'),
	url(r'^login.html$',views.login, name='index'),
	url('register',views.register, name='register'),
    url('index',views.index, name='Welcome'),
	url('calificaciones',views.calificaciones,name="calificaciones"),
]