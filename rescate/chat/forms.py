from django import forms
from chat.models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        exclude = ['personaId', 'moduleId']