from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearSolicitud', views.crearSolicitud, name='crearSolicitud'),
    path('solicitud', views.solicitudes, name='solicitudes'),
    path('calendario', views.calendario, name='calendario'),
]