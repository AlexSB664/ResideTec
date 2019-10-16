from django.db import models

from superusuario.models import Periodo, Carrera, Empresa, User
# Create your models here.


class AsesorInterno(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="carrera_del_asesorinterno")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="periodo_del_asesorinterno")

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('is_adviserI', 'Is_AdviserI'),
        )


class AsesorExterno(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="carrera_del_asesorexterno")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="periodo_del_asesorexterno")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="empresa_del_asesorexterno")

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('is_adviserE', 'Is_AdviserE'),
        )
