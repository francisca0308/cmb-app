from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()

class Module(models.Model):
    personaId = models.ForeignKey(Persona, default=1, on_delete=models.SET_DEFAULT)
    estado = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField()

class Solicitud(models.Model):
    personaId = models.ForeignKey(Persona, default=1, on_delete=models.SET_DEFAULT)
    moduleId = models.ForeignKey(Module, default=1, on_delete=models.SET_DEFAULT)
    estado = models.IntegerField(null=True, blank=True)
    fechaInicio = models.DateTimeField()
    comentario = models.TextField(max_length=280, null=True, blank=True)

class PersonModulePreference(models.Model):
    personaId = models.ForeignKey(Persona, default=1, on_delete=models.SET_DEFAULT)
    moduleId = models.ForeignKey(Module, default=1, on_delete=models.SET_DEFAULT)
    preferencia = models.IntegerField(null=True, blank=True)