from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('blogs/', views.lista_blogs, name='lista_blogs'),
    path('pages/<int:id>/', views.detalle_blog, name='detalle_blog'),
    path('crear_blog/', views.crear_blog, name='crear_blog'),
    path('actualizar_blog/<int:id>/', views.actualizar_blog, name='actualizar_blog'),
    path('eliminar_blog/<int:id>/', views.eliminar_blog, name='eliminar_blog'),
    path('knotfest/', views.knotfest, name='knotfest'),
    path('crear_artista/', views.crear_artista, name='crear_artista'),
    path('listar_artistas/', views.listar_artistas, name='listar_artistas'),
    path('actualizar_artista/<int:id>/', views.actualizar_artista, name='actualizar_artista'),
    path('eliminar_artista/<int:id>/', views.eliminar_artista, name='eliminar_artista'),
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile, name='profile'),
]
