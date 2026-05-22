from django.urls import path, include
from . import views

# Definición del espacio de nombres para la app (útil para organizar URLs)
app_name = 'catalogoMusicos'

urlpatterns = [
    path('cuenta/', include('django.contrib.auth.urls')),
    path('home/', views.mostrar_home, name='home'),

    # Ruta para el listado (ej: /catalogoMusicos/listar)
    path('musicos/', views.listar_musicos, name='listar_musicos'),
    path('musicos/<int:id>/', views.detalle_musico, name='detalle_musico'),
    path('bandas/', views.listar_bandas, name='listar_bandas'),
    path('bandas/<int:id>/', views.detalle_banda, name='detalle_banda'),
    path('anuncios/', views.listar_anuncios, name='listar_anuncios'),
    path('anuncios/<int:id>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/<int:id>/', views.detalle_evento, name='detalle_evento'),
    path('reportes/', views.listar_reportes, name='listar_reportes'),
    path('reportes/<int:id>/', views.detalle_reporte, name='detalle_reporte'),

    path('registro/', views.registro, name='registro'),
    path('registro_musico/', views.registro_musico, name='registro_musico'),
]
