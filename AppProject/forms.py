from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Artista
from .models import UserProfile, Blog

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'genero', 'descripcion']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        labels = {
            'bio': 'Biografía',
            'profile_picture': 'Foto de Perfil',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'fecha': forms.SelectDateWidget(years=range(2000, 2030)), 
        }