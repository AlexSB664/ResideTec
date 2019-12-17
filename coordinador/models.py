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

class Oferta(models.Model):
	flyer = models.ImageField(upload_to='flyers',null=True,default='default.jpeg')
	titulo = models.CharField(max_length=50,default="Oferta de Trabajo")
	descripcion = models.TextField(null=True)
	telefono_contacto = models.CharField(max_length=10,null=True)
	correo_contacto = models.CharField(max_length=100,null=True)
	vigente = models.BooleanField(default=True)
	creado = models.DateTimeField(auto_now_add=True,null=True)
	modified = models.DateTimeField(auto_now=True,null=True)
	creado_por = models.ForeignKey(User, related_name='publico_oferta', on_delete=models.CASCADE,null=True)
	carrera = models.ForeignKey(Carrera, related_name='carrera_oferta', on_delete=models.CASCADE,null=True)

	def __str__(self):
		return str(self.pk)+self.titulo