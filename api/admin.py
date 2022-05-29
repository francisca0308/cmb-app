from django.contrib import admin
from .models import Module, Persona, Solicitud, PersonModulePreference

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    fields = ['personaId', 'estado', 'fecha']

class PersonasAdmin(admin.ModelAdmin):
    fields = ['nombre','correo']

class SolicitudAdmin(admin.ModelAdmin):
    fields = ['personaId','moduleId','estado','fechaInicio','comentario']

class PersonModulePreferenceAdmin(admin.ModelAdmin):
    fields = ['personaId','moduleId','preferencia']

admin.site.register(Module, ModuleAdmin)
admin.site.register(Persona, PersonasAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(PersonModulePreference, PersonModulePreferenceAdmin)