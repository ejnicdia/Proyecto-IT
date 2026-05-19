from django.shortcuts import render, get_object_or_404
from .models import Musico, Usuario, Banda, Anuncio, Reporte, Evento

# Create your views here.

def listar_musicos(request):
    return None

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 
                  'catalogoMusicos/usuario/lista.html', 
                  {'usuarios', usuarios})

def listar_bandas(request):
    bandas = Banda.objects.all()
    return render(request,
        'catalogoMusicos/bandas/lista.html',
        {'bandas': bandas})

def listar_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request,
        'catalogoMusicos/anuncios/lista.html',
        {'anuncios': anuncios})

def listar_reportes(request):
    reportes = Reporte.objects.all()
    return render(request,
        'catalogoMusicos/reportes/lista.html',
        {'reportes': reportes})

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request,
        'catalogoMusicos/eventos/lista.html',
        {'eventos': eventos})




"""
def lista_articulos(request):
    # Usas el manager personalizado 'publicados' que creaste en la EPD 02
    articulos = Articulo.publicados.all()
    return render(request,
        'blog/articulo/lista.html',
        {'articulos': articulos})# Vista para el detalle de un artículo

def detalle_articulo(request, id):
    # Se intenta recuperar el artículo por ID. Si no existe, lanza un error 404 automáticamente.
    articulo = get_object_or_404(Articulo,
        id=id,
        estado=Articulo.Estado.PUBLICADO)
    return render(request,
        'blog/articulo/detalle.html',
        {'articulo': articulo})
"""