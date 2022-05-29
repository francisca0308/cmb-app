from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Persona, Module, PersonModulePreference, Solicitud
from .serializers import *

import json

# Create your views here.

@api_view(['GET'])
def index(request):
    data = Module.objects.all()
    serializer = ModuleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def loadPreferences(request):
    if request.method == 'GET':
        data = Module.objects.all()
        serializer = ModuleSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def editPreferences(self, request, moduleId):
    module_instance = self.get_object(moduleId)
    if not module_instance:
        return Response(
            {"res": "Este módulo no existe"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    data = {
        'personaId': request.data.get('personaId'),
        'estado': request.data.get('estado'),
        'fecha': request.data.get('fecha')
    }
    serializer = ModuleSerializer(instance = module_instance, data=data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllModules(request):
    data = Module.objects.all()
    serializer = ModuleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSolicitud(request):
    data = Solicitud.objects.all()
    serializer = SolicitudSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def getMatchedModules(request):
    if request.method == 'GET':
        solicitudes = Solicitud.objects.filter(estado=0)
        preferencias = PersonModulePreference.objects.all()

        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        id1 = request.data.get('Id1')
        id2 = request.data.get('Id2')