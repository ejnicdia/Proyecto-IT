from django.urls import path
from . import views

# Definición del espacio de nombres para la app (útil para organizar URLs)
app_name = 'catalogoMusicos'

urlpatterns = [
    # Ruta para el listado (ej: /catalogoMusicos/listar)
    path('musicos/', views.listar_musicos, name='listar_musicos'),
]