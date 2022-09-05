from django.shortcuts import render

# Create your views here.

def Inicio(request):

    return render(request, 'Inicio.html')

def facundonunez(request):

    return render(request, 'facundonunez.html')

def facundocoquet(request):

    return render(request, 'facundocoquet.html')

def federicomaguera(request):

    return render(request, 'federicomaguera.html')