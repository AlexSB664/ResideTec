from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class Carrera(models.Model):
    nombre = models.CharField(max_length=100, null=True, default='null')
    logo = models.ImageField(
        upload_to='logos', null=True, default='default.png')

    def __str__(self):
        return self.nombre


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, nombre_usuario, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        if not nombre_usuario:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.nombre_usuario = nombre_usuario
        user.password = password
        # user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre_usuario, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, nombre_usuario, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    nombre_usuario = models.CharField(unique=True, null=True, max_length=50)
    nombres = models.CharField(max_length=100, null=True)
    apellido_paterno = models.CharField(max_length=100, null=True)
    apellido_materno = models.CharField(max_length=100, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=11, null=True)
    genero = models.CharField(max_length=65, null=True)
    foto_perfil = models.ImageField(
        upload_to='profiles', null=True, default='default.jpeg')
    agregado = models.DateTimeField(default=datetime.now, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,
                                blank=True, null=True, related_name="carrera_del_usuario")
    __original_password = None

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_usuario']
    objects = MyUserManager()

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.__original_password = self.password

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno

    def get_short_name(self):
        return self.nombres

    def save(self, *args, **kwargs):
        if (self.password != self.__original_password):
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)


class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    detalle = models.CharField(max_length=100)  # Month and year period

    def __str__(self):
        return self.detalle


class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    giro = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
