from django.contrib import admin

# Register your models here.
from .models import Entrada, Estudios, Experiencia, Persona, Portfolio, Contacto
admin.site.register(Estudios)
admin.site.register(Experiencia)
admin.site.register(Portfolio)
admin.site.register(Contacto)
admin.site.register(Persona)
admin.site.register(Entrada)