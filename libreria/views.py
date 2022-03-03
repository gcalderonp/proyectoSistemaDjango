from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import libroForm

# Create your views here.

def inicio(request):

    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})

def create(request):

    libroform = libroForm(request.POST or None, request.FILES or None)

    if libroform.is_valid():
        libroform.save()
        return redirect('libros')
    
    return render(request, 'libros/crear.html', {'formulario':libroForm})

def edit(request, id):

    librorec = libro.objects.get(id=id)
    formulario = libroForm(request.POST or None, request.FILES or None, instance=libro)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    
    return render(request, 'libros/editar.html', {'formulario':formulario})

def delete(request, id):
    libroel = libro.objects.get(id=id)
    libroel.delete()
    return redirect('libros')