from django.urls import path
from .views import index, loadPreferences, editPreferences, getAllModules, getAllSolicitud, getMatchedModules

urlpatterns = [
    path('', index),
    path('loadPreferences', loadPreferences),
    path('editPreferences', editPreferences),
    path('getAllModules', getAllModules),
    path('getAllSolicitud', getAllSolicitud),
    path('getMatchedModules', getMatchedModules),
]