import py_compile
from django import views
from django.urls import path
from App1.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name="Inicio.html"),
    path('facundonunez', facundonunez, name="facundonunez.html"),
    path('facundocoquet', facundocoquet, name="facundocoquet.html"),
    path('federicomaguera', federicomaguera, name="federicomaguera.html"),
    path('estudios/', estudios, name="estudios.html"),
    path('experiencia', experiencia, name="experiencia.html"),
    path('portfolio', portafolio, name="portfolio.html"),
    path('busquedaexperiencia', busquedaexperiencia, name="busquedaexperiencia"),
    path('buscar/',buscar),
    path('eliminar/<titulo>/',eliminar,name ="eliminar")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)