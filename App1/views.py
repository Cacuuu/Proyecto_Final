from pdb import post_mortem
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render



from App1.forms import estudiosform
from App1.models import Estudios
from App1.forms import experienciaform
from App1.models import Experiencia
from App1.forms import portfolioform
from App1.models import Portfolio
from App1.models import Entrada
from App1.forms import Entradaform
# Create your views here.

def add_post (request):
    context ={}
    context['form']= Entradaform()
    return render(request,"add_post.html", context)

def home (request):
    articulos = Entrada.objects.all()
    return render(request,"bienvenida.html",{"articulos":articulos})

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

        estudios= Estudios.objects.all()

        form = estudiosform()

    return render(request, 'estudios.html', {"formulario":form,'estudios': estudios})
    

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

    return render(request, 'experiencia.html', {"formulario":form})

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