from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from chat.models import Persona, Module, Solicitud
from chat.forms import SolicitudForm
from django.contrib.auth import authenticate, login,logout


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def crearSolicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.lost_pet_id = request.user
            new_pet.save()
            messages.success(request, 'Tu solicitud se ha subido correctamente :D')
            return redirect('index')
        else:
            messages.warning(request, 'Tu solicitud no se pudo subir correctamente D:')
            return redirect('index')
    else:
        form = SolicitudForm()

    return render(request, 'crearSolicitud.html', {'form': form})

def solicitudes(request):
    query = Solicitud.objects.filter(estado=0)
    return render(request, 'solicitudes.html', {'query': query})

def calendario(request):
    query = Module.objects.all()
    return render(request, 'calendario.html', {'query': query})