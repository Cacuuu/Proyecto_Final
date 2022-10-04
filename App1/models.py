from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

class Persona(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()


class Estudios(models.Model):
    persona= models.CharField(max_length=30,default='SOME STRING')
    titulo= models.CharField(max_length=30)
    institucion= models.CharField(max_length=30)
    año_comienzo= models.DateField()
    año_finalizacion= models.DateField()

class Experiencia(models.Model):
    persona= models.CharField(max_length=30,default='SOME STRING')
    puesto= models.CharField(max_length=30)
    empresa= models.CharField(max_length=30)
    año_comienzo= models.DateField()
    año_finalizacion= models.DateField()

class Portfolio(models.Model):
    persona= models.CharField(max_length=30,default='SOME STRING')
    proyecto= models.URLField()
    habilidades= models.CharField(max_length=30)
    año= models.DateField()

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    numero= models.BigIntegerField()
    instagram= models.CharField(max_length=30,default='SOME STRING')

class Entrada(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=400)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self): 
        return reverse('home', args=(str(self.id)))
