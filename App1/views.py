from django.shortcuts import render

# Create your views here.

def Inicio(request):

    return render(request, 'Inicio.html')

def facundonunez(request):

    return render(request, 'facundonunez.html')