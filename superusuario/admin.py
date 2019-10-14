from django.contrib import admin
from .models import MyUserManager,User,Carrera,Institucion,Periodo,Empresa
# Register your models here.

#admin.site.register(MyUserManager)
admin.site.register(User)
admin.site.register(Carrera)
admin.site.register(Institucion)
admin.site.register(Periodo)
admin.site.register(Empresa)
