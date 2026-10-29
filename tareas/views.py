
from django.shortcuts import render, get_object_or_404

from .models import (
    Proyecto,
    Tarea,
    Usuario,
    AsignacionTarea,
    Comentario,
    Etiqueta,
)


def inicio(request):
    proyectos = Proyecto.objects.all()
    tareas = Tarea.objects.all()

    return render(request, 'tareas/index.html', {
        'proyectos': proyectos,
        'tareas': tareas,
    })


def lista_proyectos(request):
    proyectos = Proyecto.objects.all().order_by('nombre')

    return render(request, 'tareas/proyectos.html', {
        'proyectos': proyectos,
    })


def tareas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    tareas = Tarea.objects.filter(
        proyecto=proyecto
    ).order_by('-fecha_creacion')

    return render(request, 'tareas/tareas_proyecto.html', {
        'proyecto': proyecto,
        'tareas': tareas,
    })


def usuarios_asignados(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    asignaciones = (
        AsignacionTarea.objects
        .filter(tarea=tarea)
        .select_related('usuario')
        .order_by('fecha_asignacion')
    )

    return render(request, 'tareas/usuarios_asignados.html', {
        'tarea': tarea,
        'asignaciones': asignaciones,
    })



def buscar_observaciones(request):
    termino = request.GET.get('q', '').strip()
    tareas = Tarea.objects.none()

    if termino:
        tareas = Tarea.objects.filter(
            observaciones__icontains=termino
        ).order_by('id')

    return render(request, 'tareas/observaciones.html', {
        'tareas': tareas,
        'termino': termino,
    })


def tareas_completadas_anios(request):
    anio_inicio = request.GET.get('anio_inicio', '')
    anio_fin = request.GET.get('anio_fin', '')
    tareas = Tarea.objects.none()

    if anio_inicio.isdigit() and anio_fin.isdigit():
        tareas = Tarea.objects.filter(
            estado='Completada',
            fecha_creacion__year__gte=int(anio_inicio),
            fecha_creacion__year__lte=int(anio_fin)
        ).order_by('fecha_creacion')

    return render(request, 'tareas/completadas_anios.html', {
        'tareas': tareas,
        'anio_inicio': anio_inicio,
        'anio_fin': anio_fin,
    })



def ultimo_comentario(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    comentario = (
        Comentario.objects
        .filter(tarea__proyecto=proyecto)
        .select_related('autor', 'tarea')
        .order_by('-fecha_comentario', '-id')
        .first()
    )

    usuario = comentario.autor if comentario else None

    return render(request, 'tareas/ultimo_comentario.html', {
        'proyecto': proyecto,
        'comentario': comentario,
        'usuario': usuario,
    })


def comentarios_filtrados(request):
    palabra = request.GET.get('palabra', '').strip()
    anio = request.GET.get('anio', '').strip()
    comentarios = Comentario.objects.none()

    if palabra and anio.isdigit():
        comentarios = (
            Comentario.objects
            .filter(
                contenido__istartswith=palabra,
                fecha_comentario__year=int(anio),
            )
            .select_related('autor', 'tarea')
            .order_by('fecha_comentario')
        )

    return render(request, 'tareas/comentario_filtrado.html', {
        'comentarios': comentarios,
        'palabra': palabra,
        'anio': anio,
    })


def etiquetas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    etiquetas = (
        Etiqueta.objects
        .filter(tareas__proyecto=proyecto)
        .distinct()
        .order_by('nombre')
    )

    return render(request, 'tareas/etiquetas_proyecto.html', {
        'proyecto': proyecto,
        'etiquetas': etiquetas,
    })


def usuarios_sin_tareas(request):
    usuarios = (
        Usuario.objects
        .filter(tareas_asignadas__isnull=True)
        .distinct()
        .order_by('nombre')
    )

    return render(request, 'tareas/usuarios_sin_tareas.html', {
        'usuarios': usuarios,
    })



def error_400(request, exception):
    return render(request, 'tareas/errores/400.html', status=400)


def error_403(request, exception):
    return render(request, 'tareas/errores/403.html', status=403)


def error_404(request, exception):
    return render(request, 'tareas/errores/404.html', status=404)


def error_500(request):
    return render(request, 'tareas/errores/500.html', status=500)
