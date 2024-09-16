Este proyecto es una aplicación web creada con Django que incluye un blog, gestión de 
artistas, y funcionalidad de usuario. Permite a los usuarios autenticados crear y 
gestionar blogs y artistas, y proporciona secciones informativas sobre el festival 
Knotfest y la banda Slipknot.

Estructura del Proyecto
Directorios y Archivos Principales
appproject/
static/ - Archivos estáticos como CSS y JavaScript.
templates/ - Plantillas HTML.
views.py - Funciones de vista para manejar la lógica de las páginas web.
urls.py - Definición de URLs para las vistas.

Plantillas
padre.html - Plantilla base utilizada para el diseño general de la página. Incluye 
navegación, pie de página, y un bloque de contenido que cambia según la página.

Vistas
Inicio (inicio): Página principal del sitio.
Knotfest (knotfest): Información sobre el festival Knotfest.
Acerca de mí (about): Información sobre los creadores del proyecto.
Blogs (lista_blogs): Lista de blogs con opciones para crear, editar y eliminar.
Crear Blog (crear_blog): Página para crear un nuevo blog.
Artistas (crear_artista, listar_artistas): Gestión de artistas, incluyendo 
opciones para crear, actualizar y eliminar.

Formularios
Iniciar Sesión (IniciarSesionForm): Formulario para que los usuarios inicien sesión.
Registro (RegistroForm): Formulario para el registro de nuevos usuarios.
Crear Artista (ArtistaForm): Formulario para añadir nuevos artistas.
Crear Blog (BlogForm): Formulario para añadir nuevos blogs.

Instalación
Clonar el Repositorio
git clone https://github.com/GonzaloGalarzaGalmes/Proyecto-Final-Gonzalo-Galarza-Galmes.git


Crear y Activar un Entorno Virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar Dependencias
pip install -r requirements.txt

Aplicar Migraciones
python manage.py migrate

El super usuario es: 
user: Gonzalo
password: LilPeep21.