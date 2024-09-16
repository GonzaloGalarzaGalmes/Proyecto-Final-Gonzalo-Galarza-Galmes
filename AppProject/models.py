from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='blogs/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username