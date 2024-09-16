from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,logout,  login as auth_login
from .models import Blog, Artista, UserProfile
from .forms import ArtistaForm, CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm, BlogForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'appproject/padre.html')

def padre(request):
    return render(request, 'appproject/padre.html')

def knotfest(request):
    return render(request, 'appproject/knotfest.html')

def about(request):
    return render(request, 'appproject/about.html')

def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'appproject/lista_blogs.html', {'blogs': blogs})


def detalle_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'appproject/detalle_blog.html', {'blog': blog})

@login_required
def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_blogs')
    else:
        form = BlogForm()
    return render(request, 'appproject/crear_blog.html', {'form': form})

@login_required
def actualizar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('lista_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'appproject/actualizar_blog.html', {'form': form})

@login_required
def eliminar_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('lista_blogs')
    return render(request, 'appproject/eliminar_blog.html', {'blog': blog})


def listar_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'appproject/listar_artistas.html', {'artistas': artistas})


def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas')  
    else:
        form = ArtistaForm()
    return render(request, 'appproject/crear_artista.html', {'form': form})


def actualizar_artista(request, id):
    artista = get_object_or_404(Artista, id=id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas') 
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'appproject/actualizar_artista.html', {'form': form})


def eliminar_artista(request, id):
    artista = get_object_or_404(Artista, id=id)
    if request.method == 'POST':
        artista.delete()
        return redirect('inicio')
    return render(request, 'appproject/eliminar_artista.html', {'artista': artista})

def signup_request(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'appproject/signup.html', {'form': form})

def login_request(request):
    msg_login = ""
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('inicio')  
        else:
            msg_login = "Usuario o contraseña incorrectos"
    else:
        form = CustomAuthenticationForm()
    return render(request, 'appproject/login.html', {'form': form, "msg_login": msg_login})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'appproject/profile.html', {'form': form, 'user': request.user})

def logout_request(request):
    logout(request)
    return redirect('inicio')