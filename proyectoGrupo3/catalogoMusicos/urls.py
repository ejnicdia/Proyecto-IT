from django.urls import path, include
from . import views

# Definición del espacio de nombres para la app (útil para organizar URLs)
app_name = 'catalogoMusicos'

urlpatterns = [
    path('cuenta/', include('django.contrib.auth.urls')),
    path('', views.mostrar_home, name='home'),

    # Rutas para los CRUD de los modelos (ej: /catalogoMusicos/listar)
    path('musicos/crear/', views.crear_musico, name='crear_musico'),
    path('musicos/<int:id>/editar/', views.editar_musico, name='editar_musico'),
    path('musicos/<int:id>/eliminar/', views.eliminar_musico, name='eliminar_musico'),
    path('musicos/<int:id>/', views.detalle_musico, name='detalle_musico'),
    path('musicos/', views.listar_musicos, name='listar_musicos'),
    
    path('bandas/crear/', views.crear_banda, name='crear_banda'),
    path('bandas/<int:id>/editar/', views.editar_banda, name='editar_banda'),
    path('bandas/<int:id>/eliminar/', views.eliminar_banda, name='eliminar_banda'),
    path('bandas/<int:id>/', views.detalle_banda, name='detalle_banda'),
    path('bandas/', views.listar_bandas, name='listar_bandas'),

    path('anuncios/', views.listar_anuncios, name='listar_anuncios'),
    path('anuncios/<int:id>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('anuncios/crear/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncios/<int:id>/editar/', views.editar_anuncio, name='editar_anuncio'),
    path('anuncios/<int:id>/eliminar/', views.eliminar_anuncio, name='eliminar_anuncio'),

    path('reportes/', views.listar_reportes, name='listar_reportes'),
    path('reportes/<int:id>/', views.detalle_reporte, name='detalle_reporte'),
    path('reportes/crear/', views.crear_reporte, name='crear_reporte'),
    path('reportes/<int:id>/editar/', views.editar_reporte, name='editar_reporte'),
    path('reportes/<int:id>/eliminar/', views.eliminar_reporte, name='eliminar_reporte'),

    # Metodos de registro
    path('registro/', views.registro, name='registro'),
    path('registro_musico/', views.registro_musico, name='registro_musico'),
    
    # Rutas de creación, edición y eliminación de eventos
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:id>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('eventos/<int:id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
]
