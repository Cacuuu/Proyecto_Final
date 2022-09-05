from django.urls import path
from App1.views import *

urlpatterns = [
    path('', Inicio, name="Inicio.html"),
    path('facundonunez', facundonunez, name="facundonunez.html"),
    path('facundocoquet', facundocoquet, name="facundocoquet.html"),
    path('federicomaguera', federicomaguera, name="federicomaguera.html"),
    path('estudios', estudios, name="estudios.html")
]