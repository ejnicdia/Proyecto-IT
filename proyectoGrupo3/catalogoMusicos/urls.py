from django.urls import path
from . import views

# Definición del espacio de nombres para la app (útil para organizar URLs)
app_name = 'catalogoMusicos'

urlpatterns = [
    # Ruta para el listado (ej: /catalogoMusicos/listar)
    path('musicos/', views.listar_musicos, name='listar_musicos'),
    path('bandas/', views.listar_bandas, name='listar_bandas'),
    path('anuncios/', views.listar_anuncios, name='listar_anuncios'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('reportes/', views.listar_reportes, name='listar_reportes'),
]
