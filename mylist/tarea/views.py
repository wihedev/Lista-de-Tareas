from django.shortcuts import render, redirect
from .models import Tarea



def lista(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea.html', {'tareas': tareas})

def crear_tarea(request):
    tareas = Tarea(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    tareas.save()
    return redirect('/tarea/')

def borrar_tarea(request, id):
    tareas = Tarea.objects.get(id=id)
    tareas.delete()
    return redirect('/tarea/')









