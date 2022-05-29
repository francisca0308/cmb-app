from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearSolicitud/<int:moduleId>/<int:personaId>/', views.crearSolicitud, name='crearSolicitud'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('calendario', views.calendario, name='calendario'),
]