from django.db import models

# Create your models here.

from superusuario.models import User,Carrera,Institucion,Empresa,Periodo
from asesor.models import AsesorInterno,AsesorExterno


class Proyecto(models.Model):
	nombre = models.CharField(max_length=200,null=True)
	descripcion = models.TextField(null=True)
	# institucion
	institucion =  models.ForeignKey(Institucion,on_delete=models.CASCADE,blank=True, null=True, related_name="institucion_del_alumno")
	# empresa 
	empresa =  models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True, related_name="empresa_del_alumno")
	# periodo 
	periodo =  models.ForeignKey(Periodo,on_delete=models.CASCADE,blank=True, null=True, related_name="periodo_del_alumno")
	# asesori
	asesori =  models.ForeignKey(AsesorInterno,on_delete=models.CASCADE,blank=True, null=True, related_name="asesorinterno_del_alumno")
	# asesore
	asesore =  models.ForeignKey(AsesorExterno,on_delete=models.CASCADE,blank=True, null=True, related_name="asesorexterno_del_alumno")
	# status
	estatus = models.CharField(max_length=50,null=True)
	terminado = models.BooleanField(null=False,default=False)

	def __str___(self):
		return self.nombre

class Alumno(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	NoControl = models.CharField(max_length=8,null=True, blank=True,unique=True)
	carrera =  models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_del_alumno")
	semetre = models.IntegerField(null=True)
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,blank=True, null=True, related_name="proyecto_del_alumno")

	def __str__(self):
		return  self.NoControl+self.email.email
	class Meta:
		permissions = (
			('is_student', 'Is_Student'),
        )