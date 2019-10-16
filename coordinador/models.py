from django.db import models

from superusuario.models import Carrera, User

# Create your models here.

class Coordinador(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,blank=True, null=True, related_name="carrera_administra")
	
	def __str__(self):
		return self.email.email
		
	class Meta:
		permissions = (
			('is_admin', 'Is_Admin'),
		)
