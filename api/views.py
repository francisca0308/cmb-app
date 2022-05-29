from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Persona, Module
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

@api_view(['GET','PUT'])
def editPreferences(request):
    if request.method == 'GET':
        data = Module.objects.all()
        serializer = ModuleSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)