"""ResideTec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import superusuario.views
#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^logout$', logout_then_login, name='logout' ),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], superusuario.views.protected_serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^',include('alumno.urls' )),
    url(r'^',include('asesor.urls' )),
    url(r'^',include('coordinador.urls' )),    
]
