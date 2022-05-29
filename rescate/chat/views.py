from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from chat.models import Persona, Module, Solicitud
from chat.forms import SolicitudForm


def index(request):
    return render(request, "index.html")

def crearSolicitud(request, moduleId, personaId):
    module = get_object_or_404(Module, pk=moduleId)
    persona = get_object_or_404(Persona, pk=personaId)
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            nuevaSolicitud = form.save(commit=False)
            nuevaSolicitud.personaId = persona
            nuevaSolicitud.moduleId = module
            nuevaSolicitud.save()
            messages.success(request, 'Tu solicitud se ha subido correctamente :D')
            return redirect('solicitudes')
        else:
            messages.warning(request, 'Tu solicitud no se pudo subir correctamente D:')
            return redirect('solicitudes')
    else:
        form = SolicitudForm()

    return render(request, 'crearSolicitud.html', {'form': form})

def solicitudes(request):
    query = Solicitud.objects.filter(estado=0)
    return render(request, 'solicitudes.html', {'query': query})

def calendario(request):
    query = Module.objects.all()
    personas = Persona.objects.all()
    return render(request, 'calendario.html', {'query': query})