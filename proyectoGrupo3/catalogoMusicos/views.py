from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.conf import settings
from .models import Musico, Banda, Anuncio, Reporte, Evento
from .forms import BandaForm, AnuncioForm, ReporteForm, EventoForm, FormularioRegistro, FormularioRegistroMusico
# from .forms import MusicoForm 
# Comentado todo lo que tiene que ver con musicoForm. Por ahora un perfil no puede crear musicos, si no que se dan de alta ellos.

def mostrar_home(request):
    return render(request, 'catalogoMusicos/home.html', {})

def registro(request):
    if request.method == 'POST':
        form_registro = FormularioRegistro(request.POST)
        if form_registro.is_valid():
            
            # Creas el objeto en memoria, estableces la contraseña (con el hash seguro) y lo guardas
            nueva_cuenta = form_registro.save(commit=False)
            nueva_cuenta.set_password(form_registro.cleaned_data['password']) # Encripta la contraseña.
            nueva_cuenta.save()
            return render(request, 'catalogoMusicos/registro_completado.html', {'nueva_cuenta': nueva_cuenta})
    else:
        form_registro = FormularioRegistro()
    return render(request, 'catalogoMusicos/registro.html', {'form_registro': form_registro})

def registro_musico(request):
    if request.method == 'POST':
        form_registro = FormularioRegistroMusico(request.POST)
        if form_registro.is_valid():
            
            # Creas el objeto en memoria, estableces la contraseña (con el hash seguro) y lo guardas
            nueva_cuenta = form_registro.save(commit=False)
            nueva_cuenta.set_password(form_registro.cleaned_data['password']) # Encripta la contraseña.
            nueva_cuenta.save()
            return render(request, 'catalogoMusicos/registro_completado.html', {'nueva_cuenta': nueva_cuenta})
    else:
        form_registro = FormularioRegistroMusico()
    return render(request, 'catalogoMusicos/registro_musico.html', {'form_registro': form_registro})

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
    bandas = evento.bandas.all()
    context = {
        'evento': evento,
        'bandas': bandas,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request,
        'catalogoMusicos/eventos/detalle.html',
        context)

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

"""
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
"""

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(data=request.POST, user=request.user)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.save()
            form.save_m2m()  # Guardar la relación ManyToMany con bandas
            messages.success(request, f'¡Evento "{evento.titulo}" creado exitosamente!')
            return redirect('catalogoMusicos:listar_eventos')
    else:
        form = EventoForm(user=request.user)
    
    return render(request, 'catalogoMusicos/eventos/crear.html', {
        'form': form,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
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
            return redirect('catalogoMusicos:detalle_reporte', id=reporte.id)
    else:
        form = ReporteForm(instance=reporte)
        
    return render(request, 'catalogoMusicos/reportes/editar.html', {
        'form': form,
        'reporte': reporte
    })

"""
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
"""

@login_required
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    # Validar propiedad
    if evento.usuario != request.user:
        raise PermissionDenied("No tienes permiso para editar este evento.")
        
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('catalogoMusicos:detalle_evento', id=evento.id)
    else:
        form = EventoForm(instance=evento, user=request.user)
        
    return render(request, 'catalogoMusicos/eventos/editar.html', {
        'form': form,
        'evento': evento,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
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
            return redirect('catalogoMusicos:detalle_anuncio', id=anuncio.id)
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
            return redirect('catalogoMusicos:detalle_banda', id=banda.id)
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
        return redirect('catalogoMusicos:listar_reportes')
        
    return render(request, 'catalogoMusicos/reportes/eliminar.html', {'reporte': reporte})


@login_required
def eliminar_musico(request, id):
    musico = get_object_or_404(Musico, id=id)
    
    if musico.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este perfil de músico.")
        
    if request.method == 'POST':
        musico.delete()
        return redirect('catalogoMusicos:listar_musicos')
        
    return render(request, 'catalogoMusicos/musicos/eliminar.html', {'musico': musico})


@login_required
def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if evento.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este evento.")
        
    if request.method == 'POST':
        evento.delete()
        return redirect('catalogoMusicos:listar_eventos')
        
    return render(request, 'catalogoMusicos/eventos/eliminar.html', {'evento': evento})


@login_required
def eliminar_anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    
    if anuncio.usuario != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este anuncio.")
        
    if request.method == 'POST':
        anuncio.delete()
        return redirect('catalogoMusicos:listar_anuncios')
        
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
        return redirect('catalogoMusicos:listar_bandas')
        
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