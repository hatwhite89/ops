"""ops URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from ops import settings
from opsApp import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url('^admin/', admin.site.urls),
    url(r'^ayuda/$', views.help, name='ayuda'),
    url(r'^pagina_contenido/$', views.paginaContenido, name="pagina_contenido"),
    url(r'^archivos/$', views.archivo, name="archivos"),
    url(r'^lnme/$', views.listadoNacionalMedicamentos, name="lnme"),
    url(r'^lnme_original/$', views.listadoNacionalMedicamentos531, name="lnme531"),
    url(r'^lnme2/$', views.listadoNacionalMedicamentos2, name="lnme2"),
    url(r'^lnme3/$', views.listadoNacionalMedicamentos3, name="lnme3"),
    url(r'^politicas/$', views.politicas, name="politicas"),
    url(r'^sugerencia/$', views.sugerencias_view, name="sugerencia"),
    url(r'^respuesta_sugerencia/$', views.correoSugerencia, name="respuesta_sugerencia"),
    url(r'^lnm_detalle/$', views.listadoNacionalMedicamentosDetalle, name="lnm_detalle"),
    url(r'^lnm_detalle3/$', views.listadoNacionalMedicamentosDetalle3, name="lnm_detalle3"),
    url(r'^busqueda/$', views.search, name='busquedaProyecto'),
    url(r'^detalle_busqueda/$', views.detalleBuscador, name='detalle_busqueda'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)