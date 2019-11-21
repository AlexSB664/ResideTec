from django.db import models

from superusuario.models import Carrera, User

# Create your models here.

class Coordinador(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.email.email
		
	class Meta:
		permissions = (
			('is_admin', 'Is_Admin'),
		)
