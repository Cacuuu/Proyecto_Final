from django import views
from django.urls import path
from App1.views import *

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
    path('blog/', home, name="bienvenida.html"),
    path('add_post/', add_post, name="add_post.html"),
]