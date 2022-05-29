from django.contrib import admin
from .models import Module, Persona, Solicitud

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    fields = ['personaId', 'estado', 'fecha']

class PersonasAdmin(admin.ModelAdmin):
    fields = ['nombre','correo']

class SolicitudesAdmin(admin.ModelAdmin):
    fields = ['personaId','moduleId','estado','fechaInicio','comentario']

admin.site.register(Module, ModuleAdmin)
admin.site.register(Persona, PersonasAdmin)
admin.site.register(Solicitud, SolicitudesAdmin)