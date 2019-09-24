from django.contrib import admin
from .models import MyUserManager,User,Carrera
# Register your models here.

#admin.site.register(MyUserManager)
admin.site.register(User)
admin.site.register(Carrera)

