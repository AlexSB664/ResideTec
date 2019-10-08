from django.db import models

# Create your models here.

from superusuario.models import User,Carrera



class Proyecto(models.Model):
	nombre = models.CharField(max_length=200,null=True)
	descripcion = models.TextField(null=True)
	# institucion
	# empresa 
	# periodo 
	# asesori
	# asesore
	# status
	def __str___(self):
		return self.nombre

class Alumno(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=8,null=True, blank=True,unique=True)
	carrera =  models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_del_alumno")
	semetre = models.IntegerField(null=True)
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,blank=True, null=True, related_name="proyecto_del_alumno")

	def __str__(self):
		return  self.matricula+self.email.email