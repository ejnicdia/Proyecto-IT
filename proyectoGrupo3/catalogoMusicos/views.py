from django.shortcuts import render
from .models import Musico, Usuario, Banda, Anuncio, Reporte, Evento

# Create your views here.

def listar_musicos(request):
    return None

def listar_usuarios(request):
    return None

def listar_bandas(request):
    return None

def listar_anuncios(request):
    return None

def listar_reportes(request):
    return None

def listar_eventos(request):
    return None

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