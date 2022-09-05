from typing import Dict
from django.shortcuts import render

from App1.forms import estudiosform
from App1.models import Estudios
from App1.forms import experienciaform
from App1.models import Experiencia
# Create your views here.

def Inicio(request):

    return render(request, 'Inicio.html')

def facundonunez(request):

    return render(request, 'facundonunez.html')

def facundocoquet(request):

    return render(request, 'facundocoquet.html')

def federicomaguera(request):

    return render(request, 'federicomaguera.html')

def estudios(request):

    if request.method == 'POST':

        form = estudiosform(request.POST)

        print(form)

        if form.is_valid:

            data= form.cleaned_data

            estudio1= Estudios(persona=data['persona'],
            titulo=data['titulo'],
            institucion=data['institucion'],
            año_comienzo=data['año_comienzo'],
            año_finalizacion=data['año_finalizacion'],)
            estudio1.save() 

            return render(request, "Inicio.html")

    else:

        form = estudiosform()

    return render(request, 'estudios.html', {"formulario":form})

def experiencia(request):

    if request.method == 'POST':

        form = experienciaform(request.POST)

        print(form)

        if form.is_valid:

            data= form.cleaned_data

            experiencia1 = Experiencia(experiencia=data['experiencia'],
            puesto=data['puesto'],
            empresa=data['empresa'],
            año_comienzo=data['año_comienzo'],
            año_finalizacion=data['año_finalizacion'],)
            experiencia1.save() 

            return render(request, "Inicio.html")

    else:

        form = experienciaform()

    return render(request, 'estudios.html', {"formulario":form})