import py_compile
from django import views
from django.urls import path
from App1.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name="Inicio.html"),
    path('facundonunez/', facundo_nunez, name="facundonunez.html"),
    path('facundocoquet/', facundo_coquet, name="facundocoquet.html"),
    path('federicomaguera/', federico_maguera, name="federicomaguera.html"),
    path('estudios/', EstudiosList.as_view(), name="estudios.html"),
    path('experiencia/', ExperienciaList.as_view(), name="experiencia.html"),
    path('estudios-create/<int:id>/',EstudioCreate.as_view(), name ="estudio-create"),
    path('estudios-edit/<int:pk>/',EstudioEdit.as_view(), name ="estudio-edit"),
    path('estudios-eliminar/<int:pk>/',EstudioDelete.as_view(), name ="estudio-eliminar"),  
    path('experiencia-create/',ExperienciaCreate.as_view(), name ="experiencia-create"),
    path('experiencia-edit/<int:pk>/',ExperienciaUpdate.as_view(), name ="experiencia-edit"),
    path('experiencia-eliminar/<int:pk>/',ExperienciaDelete.as_view(), name ="experiencia-eliminar"),
    path('portfolio/', portafolio, name="portfolio.html"),
    path('busquedaexperiencia/', busquedaexperiencia, name="busquedaexperiencia"),
    path('buscar/',buscar),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)