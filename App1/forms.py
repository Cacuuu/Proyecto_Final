from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField



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

class portfolioform(forms.Form):
    persona= forms.CharField(max_length=30)
    proyecto= forms.URLField()
    habilidades= forms.CharField(max_length=30)
    año= forms.DateField()

from django.core.exceptions import ValidationError 
from django.views.decorators.csrf import csrf_protect


class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        help_texts = {k:"" for k in fields}

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def clean_email(self):
   # Get the email
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email = email)

        except User.DoesNotExist:

            return email
        raise forms.ValidationError('This email address is already in use.')
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  

        if len(password1) < 8:
            raise ValidationError("Password too short,try again.")  

        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match, try again.")
        return password2         
          
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  
