# Gestión de Tareas

Permite a los usuarios gestionar, organizar y realizar el seguimiento de sus tareas pendientes de forma sencilla y eficiente. A través de una interfaz interactiva y modular, la plataforma facilita la creación de nuevos ítems, la actualización de sus estados de avance y el almacenamiento persistente de la información mediante una base de datos integrada.

## 📊 Análisis de la Estructura del Proyecto

```text
GestionTareas/
├── .venv/                       # Entorno virtual de Python
├── gestion_tareas/              # Configuración principal de Django
│   ├── __pycache__/             # Archivos compilados de Python
│   ├── __init__.py              # Identifica el directorio como paquete
│   ├── asgi.py                  # Configuración para aplicaciones asíncronas
│   ├── settings.py              # Configuración global del proyecto
│   ├── urls.py                  # Enrutamiento global de URLs
│   └── wsgi.py                  # Configuración para servidores web
├── tareas/                      # Aplicación principal
│   ├── __pycache__/             # Archivos compilados de Python
│   ├── fixtures/                # Datos de prueba y copias de seguridad
│   ├── migrations/              # Migraciones de la base de datos
│   ├── templates/               # Plantillas HTML
│   │   └── tareas/
│   │       └── errors/          # Páginas de error personalizadas
│   │           ├── 400.html     # Error de petición incorrecta
│   │           ├── 403.html     # Error de acceso prohibido
│   │           ├── 404.html     # Página no encontrada
│   │           └── 500.html     # Error interno del servidor
│   ├── admin.py                 # Configuración del panel de administración
│   ├── apps.py                  # Configuración de la aplicación
│   ├── models.py                # Definición de los modelos de datos
│   ├── tests.py                 # Pruebas de funcionamiento
│   └── views.py                 # Lógica y gestión de las vistas
├── manage.py                    # Herramienta de administración de Django
├── seed.py                      # Script para cargar datos iniciales
├── db.sqlite3                   # Base de datos SQLite
└── .gitignore                   # Archivos y carpetas excluidos de Git
```
