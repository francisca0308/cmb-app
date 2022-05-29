from django.urls import path
from .views import index, loadPreferences, editPreferences

urlpatterns = [
    path('', index),
    path('loadPreferences', loadPreferences),
    path('editPreferences', editPreferences),
]