from django.db import models

from superusuario.models import Periodo,Carrera,Empresa
# Create your models here.

class AsesorInterno(models.Model):
    nombre=models.CharField(max_length=50)
    carrera =  models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_del_asesorinterno")
    correo=models.CharField(max_length=50)
    periodo =  models.ForeignKey(Periodo,on_delete=models.CASCADE,blank=True, null=True, related_name="periodo_del_asesorinterno")

    def __str__(self):
        return self.nombre

class AsesorExterno(models.Model):
    nombre=models.CharField(max_length=50)
    carrera =  models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_del_asesorexterno")
    correo=models.CharField(max_length=50)
    periodo =  models.ForeignKey(Periodo,on_delete=models.CASCADE,blank=True, null=True, related_name="periodo_del_asesorexterno")
    empresa =  models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True, related_name="empresa_del_asesorexterno")

    def __str__(self):
        return self.nombre