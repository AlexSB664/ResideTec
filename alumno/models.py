from django.db import models

# Create your models here.

from superusuario.models import User,Carrera

class Alumno(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=8,null=True)
	carrera =  models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_del_alumno")

	def __str__(self):
		return  self.matricula+self.email.email


class Proyecto(models.Model):
	nombre = models.CharField(max_length=200,null=True)
	descripcion = models.TextField(null=True)

	def __str___(self):
		return self.nombre