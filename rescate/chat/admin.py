from django.contrib import admin
from .models import Module, Persona

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    fields = ['personaId', 'estado', 'fecha']

class PersonasAdmin(admin.ModelAdmin):
    fields = ['nombre','correo']

admin.site.register(Module, ModuleAdmin)
admin.site.register(Persona, PersonasAdmin)