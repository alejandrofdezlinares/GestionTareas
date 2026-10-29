from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_proyecto, name='tareas_proyecto'),
    path('tareas/<int:tarea_id>/usuarios/', views.usuarios_asignados, name='usuarios_asignados'),
    path('tareas/por-observaciones/', views.buscar_observaciones, name='buscar_observaciones'),
    path('tareas/completadas-entre-anios/', views.tareas_completadas_anios, name='tareas_completadas_anios'),
    path('proyectos/<int:proyecto_id>/ultimo-comentario/', views.ultimo_comentario, name='ultimo_comentario'),
    path('comentarios/filtrados/', views.comentarios_filtrados, name='comentarios_filtrados'),
    path('proyectos/<int:proyecto_id>/etiquetas/', views.etiquetas_proyecto, name='etiquetas_proyecto'),
    path('usuarios/sin-tareas/', views.usuarios_sin_tareas, name='usuarios_sin_tareas'),
]

handler400 = 'tareas.views.error_400'
handler403 = 'tareas.views.error_403'
handler404 = 'tareas.views.error_404'
handler500 = 'tareas.views.error_500'
