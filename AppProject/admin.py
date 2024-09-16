from django.contrib import admin
from .models import Blog, Artista, UserProfile

admin.site.register(Blog)
admin.site.register(Artista)
admin.site.register(UserProfile)