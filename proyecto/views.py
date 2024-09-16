from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
    path('users/', include('users.urls')),
]