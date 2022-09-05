from django import forms

class estudiosform(forms.Form):
    persona= forms.CharField(max_length=30)
    titulo= forms.CharField(max_length=30)
    institucion= forms.CharField(max_length=30)
    año_comienzo= forms.DateField()
    año_finalizacion= forms.DateField()

class experienciaform(forms.Form):
    persona= forms.CharField(max_length=30)
    puesto= forms.CharField(max_length=30)
    empresa= forms.CharField(max_length=30)
    año_comienzo= forms.DateField()
    año_finalizacion= forms.DateField()
    