from ast import Del
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from App1.forms import estudiosform
from App1.models import Estudios
from App1.forms import experienciaform
from App1.models import Experiencia
from App1.forms import portfolioform
from App1.models import Portfolio
# Create your views here.

def inicio(request):

    return render(request, 'Inicio.html')

def Aboutus(request):

    return render(request, "Aboutus.html")

def facundo_nunez(request):

    return render(request, 'facundonunez.html')

def facundo_coquet(request):

    return render(request, 'facundocoquet.html')

def federico_maguera(request):

    return render(request, 'federicomaguera.html')

class EstudiosList(ListView):
    
    model= Estudios
    template_name = 'estudios.html'

class EstudioCreate(CreateView):
    
    model = Estudios
    success_url= reverse_lazy('estudios.html')
    fields = ['persona','titulo','institucion','año_comienzo','año_finalizacion']

class EstudioEdit(UpdateView):
    model = Estudios
    success_url= reverse_lazy('estudios.html')
    fields = ['persona','titulo','institucion','año_comienzo','año_finalizacion']

class EstudioDelete(DeleteView):
    model= Estudios
    success_url = reverse_lazy('estudios.html')

class ExperienciaList(ListView):

    model = Experiencia

    template_name = 'experiencia.html'

class ExperienciaCreate(CreateView):
    
    model = Experiencia
    success_url= reverse_lazy('experiencia.html')
    fields = ['persona','puesto','empresa','año_comienzo','año_finalizacion']

class ExperienciaUpdate(UpdateView):
    model = Experiencia
    success_url= reverse_lazy('experiencia.html')
    fields = ['persona','puesto','empresa','año_comienzo','año_finalizacion']

class ExperienciaDelete(DeleteView):

    model= Experiencia
    success_url = reverse_lazy('experiencia.html')


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

def eliminarexp(request,id):
    
    experiencia = Experiencia.objects.get(id=id)
    experiencia.delete()

    exp = Experiencia.objects.all()

    contexto= {"exp",exp}

    return render(request,'experiencia.html',contexto)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate


from django.contrib.auth.forms import UserCreationForm

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario Creado."})

    else:
        form= UserCreationForm()

    return render(request, "register.html", {"form":form})

from django.contrib.auth.views import LoginView,LogoutView

class AdminLogin(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('Inicio.html')

class AdminLogout(LogoutView):
    template_name = 'logout.html'

