from django.urls import path
from App1.views import *

urlpatterns = [
    path('', Inicio, name="Inicio.html"),
    path('facundonunez', facundonunez, name="Inicio.html"),
]