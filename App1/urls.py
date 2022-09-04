from django.urls import path
from App1.views import Inicio

urlpatterns = [
    path('', Inicio, name="Inicio.html"),
]