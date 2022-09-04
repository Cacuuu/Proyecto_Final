from pyexpat import model
from django.db import models

# Create your models here.

class Estudios(models.Model):
    titulo= models.CharField(max_length=30)
    institucion= models.CharField(max_length=30)
    año_comienzo= models.CharField(max_length=30)
    año_finalizacion= models.CharField(max_length=30)

class Experiencia(models.Model):
    puesto= models.CharField(max_length=30)
    empresa= models.CharField(max_length=30)
    año_comienzo= models.DateField()
    año_finalizacion= models.DateField()

class Portfolio(models.Model):
    proyecto= models.CharField(max_length=30)
    habilidades= models.CharField(max_length=30)
    año= models.DateField()

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    numero= models.BigIntegerField()
    mensaje= models.CharField(max_length=255)
