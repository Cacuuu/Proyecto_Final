from tkinter import E
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App1.forms import estudiosform
from App1.models import Estudios
from App1.forms import experienciaform
from App1.models import Experiencia
from App1.forms import portfolioform
from App1.models import Portfolio
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

    estudios= Estudios.objects.all()


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
        estudios= Estudios.objects.all()
        contexto= {"formulario":form,'estudios': estudios}


    return render(request, 'estudios.html',contexto)
    

def experiencia(request):

    exp= Experiencia.objects.all()

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

        exp= Experiencia.objects.all()
        form = experienciaform()
        contexto= {"formulario":form, "Experiencia":exp}
        
        
    return render(request, 'experiencia.html',contexto)

def portafolio(request):

    if request.method == 'POST':

        form = portfolioform(request.POST)

        print(form)

        if form.is_valid:

            data= form.cleaned_data

            persona = Portfolio(persona=data['persona'],
            proyecto=data['proyecto'],
            habilidades=data['habilidades'],
            año = data['año'])

            persona.save() 

            return render(request, "Inicio.html")

    else:

        form = portfolioform()

    return render(request, 'portfolio.html', {"formulario":form})

def busquedaexperiencia(request):

    return render(request, "busquedaexperiencia.html")

def buscar(request):

    respuesta= f"Estoy buscando el puesto {request.GET['puesto']}"

    return HttpResponse(respuesta)

def eliminar(request,titulo):
    estudio= Estudios.objects.get(titulo=titulo)
    estudio.delete()

    estudios = Estudios.objects.all()

    contexto = {"estudios":estudios}

    return render(request, "estudios.html", contexto)