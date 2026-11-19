# Gestión de Tareas

Permite a los usuarios gestionar, organizar y realizar el seguimiento de sus tareas pendientes de forma sencilla y eficiente. A través de una interfaz interactiva y modular, la plataforma facilita la creación de nuevos ítems, la actualización de sus estados de avance y el almacenamiento persistente de la información mediante una base de datos integrada.

**## Análisis de la Estructura del Proyecto**

```text
GestionTareas/
├── .venv/                            # Entorno virtual de Python
├── gestion_tareas/                    # Configuración principal de Django
│   ├── __pycache__/                   # Archivos compilados de Python
│   ├── __init__.py                    # Identifica el directorio como paquete
│   ├── asgi.py                        # Configuración para aplicaciones asíncronas
│   ├── settings.py                     # Configuración global del proyecto
│   ├── urls.py                        # Enrutamiento global de URLs
│   └── wsgi.py                        # Configuración para servidores web
├── tareas/                             # Aplicación principal
│   ├── __pycache__/                    # Archivos compilados de Python
│   ├── fixtures/                        # Datos de prueba y copias de seguridad
│   ├── migrations/                      # Migraciones de la base de datos
│   ├── templates/                        # Plantillas HTML
│   │   └── tareas/
│   │       ├── errores/                  # Páginas de error personalizadas
│   │       │   ├── 400.html              # Error de petición incorrecta
│   │       │   ├── 403.html              # Error de acceso prohibido
│   │       │   ├── 404.html              # Página no encontrada
│   │       │   └── 500.html              # Error interno del servidor
│   │       │
│   │       ├── parciales/                # Templates reutilizables
│   │       │   ├── proyecto_item.html     # Elemento de proyecto
│   │       │   ├── tarea_item.html       # Elemento de tarea
│   │       │   ├── tarea_simple.html     # Tarea simplificada
│   │       │   ├── etiqueta_item.html    # Elemento de etiqueta
│   │       │   ├── asignacion_item.html  # Elemento de asignación
│   │       │   ├── usuario_item.html     # Elemento de usuario
│   │       │   ├── comentario_item.html  # Elemento de comentario
│   │       │   └── tarea_completada_item.html
│   │       │
│   │       ├── comentario_filtrado.html
│   │       ├── completadas_anios.html
│   │       ├── etiquetas_proyecto.html
│   │       ├── index.html               # Página principal
│   │       ├── observaciones.html
│   │       ├── proyectos.html
│   │       ├── tareas_proyecto.html
│   │       ├── ultimo_comentario.html
│   │       ├── usuarios_asignados.html
│   │       ├── usuarios_sin_tareas.html
│   │       ├── navbar.html              # Menú de navegación
│   │       ├── footer.html              # Pie de página
│   │       └── base.html                # Template base
│   │
│   ├── static/                          # Recursos estáticos
│   │   └── tareas/
│   │       ├── css/
│   │       │   └── estilos.css            # Estilos de la web
│   │       ├── js/
│   │       │   └── script.js              # JavaScript
│   │       └── img/
│   │           └── logo.png               # Logo de la aplicación
│   │
│   ├── admin.py                          # Configuración del administrador
│   ├── apps.py                           # Configuración de la aplicación
│   ├── models.py                          # Definición de modelos
│   ├── tests.py                           # Pruebas de funcionamiento
│   └── views.py                            # Lógica y gestión de vistas
│
├── manage.py                              # Herramienta de administración Django
├── seed.py                                # Script para cargar datos iniciales
├── db.sqlite3                             # Base de datos SQLite
└── .gitignore                              # Archivos excluidos de Git
```

**## Templates y reutilización**

- Creación de una plantilla de navegación superior y un footer.
- Template `base.html` con bloques de cabecera y contenido.
- Herencia de la plantilla base en las diferentes páginas.
- Inclusión de CSS, JavaScript e imágenes.
- Creación de templates parciales para reutilizar elementos de tareas, proyectos, usuarios, comentarios y etiquetas mediante `include`.

**## Template Tags y operadores**

- Uso de diferentes template tags como `if`, `else`, `for` y `empty`.
- Utilización de diferentes operadores lógicos para comprobar condiciones y controlar la visualización de los datos.

**## Template Filters**

Utilización de filtros de Django para modificar y dar formato a los datos mostrados en las páginas, incluyendo fechas, textos, valores y otros elementos dinámicos.

