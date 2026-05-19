from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Musico, Banda, Anuncio, Reporte, Evento
from .forms import MusicoForm, BandaForm, AnuncioForm, ReporteForm, EventoForm

# Create your views here.

def listar_musicos(request):
    musicos = Musico.objects.all()
    return render(request, 'catalogoMusicos/Musicos/lista.html', {'musicos': musicos})

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

def detalle_musico(request, id):
    musico = get_object_or_404(Musico, id=id)
    return render(request,
        'catalogoMusicos/musicos/detalle.html',
        {'musico': musico})

def detalle_banda(request, id):
    banda = get_object_or_404(Banda, id=id)
    return render(request,
        'catalogoMusicos/bandas/detalle.html',
        {'banda': banda})

def detalle_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    return render(request,
        'catalogoMusicos/anuncios/detalle.html',
        {'anuncio': anuncio})

def detalle_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    return render(request,
        'catalogoMusicos/reportes/detalle.html',
        {'reporte': reporte})

def detalle_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request,
        'catalogoMusicos/eventos/detalle.html',
        {'evento': evento})

@login_required
@require_POST
def crear_reporte(request):
    reporte = None
    form = ReporteForm(data=request.POST)
    if form.is_valid():
        reporte = form.save(commit=False)
        reporte.usuario = request.user
        reporte.save()
        
    return render(request, 'catalogoMusicos/reportes/crear.html', {
        'form': form,
        'reporte': reporte
    })


@login_required
@require_POST
def crear_musico(request):
    musico = None
    form = MusicoForm(data=request.POST)
    if form.is_valid():
        musico = form.save(commit=False)
        musico.usuario = request.user
        musico.save()
        
    return render(request, 'catalogoMusicos/musicos/crear.html', {
        'form': form,
        'musico': musico
    })


@login_required
@require_POST
def crear_evento(request):
    evento = None
    form = EventoForm(data=request.POST)
    if form.is_valid():
        evento = form.save(commit=False)
        evento.usuario = request.user
        evento.save()
        
    return render(request, 'catalogoMusicos/eventos/crear.html', {
        'form': form,
        'evento': evento
    })


@login_required
@require_POST
def crear_anuncio(request):
    anuncio = None
    form = AnuncioForm(data=request.POST)
    if form.is_valid():
        anuncio = form.save(commit=False)
        anuncio.usuario = request.user
        anuncio.save()
        form.save_m2m() 
        
    return render(request, 'catalogoMusicos/anuncios/crear.html', {
        'form': form,
        'anuncio': anuncio
    })


@login_required
@require_POST
def crear_banda(request):
    banda = None
    form = BandaForm(data=request.POST)
    if form.is_valid():
        banda = form.save()
        
    return render(request, 'catalogoMusicos/bandas/crear.html', {
        'form': form,
        'banda': banda
    })

@login_required
def editar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    
    # Validar propiedad
    if reporte.usuario != request.user:
        raise PermissionDenied("No tienes permiso para editar este reporte.")
        
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('detalle_reporte', id=reporte.id)
    else:
        form = ReporteForm(instance=reporte)
        
    return render(request, 'catalogoMusicos/reportes/editar.html', {
        'form': form,
        'reporte': reporte
    })


@login_required
def editar_musico(request, id):
    musico = get_object_or_404(Musico, id=id)
    
    # Validar propiedad (Relación OneToOne)
    if musico.usuario != request.user:
        raise PermissionDenied("No tienes permiso para editar este perfil de músico.")
        
    if request.method == 'POST':
        form = MusicoForm(request.POST, instance=musico)
        if form.is_valid():
            form.save()
            return redirect('detalle_musico', id=musico.id)
    else:
        form = MusicoForm(instance=musico)
        
    return render(request, 'catalogoMusicos/musicos/editar.html', {
        'form': form,
        'musico': musico
    })


@login_required
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    # Validar propiedad
    if evento.usuario != request.user:
        raise PermissionDenied("No tienes permiso para editar este evento.")
        
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', id=evento.id)
    else:
        form = EventoForm(instance=evento)
        
    return render(request, 'catalogoMusicos/eventos/editar.html', {
        'form': form,
        'evento': evento
    })


@login_required
def editar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    
    # Validar propiedad
    if anuncio.usuario != request.user:
        raise PermissionDenied("No tienes permiso para editar este anuncio.")
        
    if request.method == 'POST':
        form = AnuncioForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect('detalle_anuncio', id=anuncio.id)
    else:
        form = AnuncioForm(instance=anuncio)
        
    return render(request, 'catalogoMusicos/anuncios/editar.html', {
        'form': form,
        'anuncio': anuncio
    })


@login_required
def editar_banda(request, id):
    banda = get_object_or_404(Banda, id=id)
    
    # Como Banda no tiene un 'usuario' directo, verificamos si el usuario 
    # logueado tiene un perfil de músico y si pertenece a los músicos de la banda
    try:
        if not banda.musicos.filter(usuario=request.user).exists():
            raise PermissionDenied("No tienes permiso para editar esta banda porque no eres miembro.")
    except AttributeError:
        raise PermissionDenied("Debes tener un perfil de músico asociado para gestionar bandas.")
        
    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('detalle_banda', id=banda.id)
    else:
        form = BandaForm(instance=banda)
        
    return render(request, 'catalogoMusicos/bandas/editar.html', {
        'form': form,
        'banda': banda
    })


@login_required
def eliminar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    
    if reporte.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este reporte.")
        
    if request.method == 'POST':
        reporte.delete()
        return redirect('listar_reportes')
        
    return render(request, 'catalogoMusicos/reportes/eliminar.html', {'reporte': reporte})


@login_required
def eliminar_musico(request, id):
    musico = get_object_or_404(Musico, id=id)
    
    if musico.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este perfil de músico.")
        
    if request.method == 'POST':
        musico.delete()
        return redirect('listar_musicos')
        
    return render(request, 'catalogoMusicos/musicos/eliminar.html', {'musico': musico})


@login_required
def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if evento.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este evento.")
        
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
        
    return render(request, 'catalogoMusicos/eventos/eliminar.html', {'evento': evento})


@login_required
def eliminar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    
    if anuncio.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este anuncio.")
        
    if request.method == 'POST':
        anuncio.delete()
        return redirect('listar_anuncios')
        
    return render(request, 'catalogoMusicos/anuncios/eliminar.html', {'anuncio': anuncio})


@login_required
def eliminar_banda(request, id):
    banda = get_object_or_404(Banda, id=id)
    
    try:
        if not banda.musicos.filter(usuario=request.user).exists():
            raise PermissionDenied("No tienes permiso para eliminar esta banda porque no eres miembro.")
    except AttributeError:
        raise PermissionDenied("Debes tener un perfil de músico asociado para gestionar bandas.")
        
    if request.method == 'POST':
        banda.delete()
        return redirect('listar_bandas')
        
    return render(request, 'catalogoMusicos/bandas/eliminar.html', {'banda': banda})


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