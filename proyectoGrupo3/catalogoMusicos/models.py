from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Reporte(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion_error = models.TextField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    # Relaciones 
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Reportes'
    )

    def __str__(self):
        return self.titulo
    
class Musico(User):
    instrumento = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    fecha_inicio_estudio = models.DateField()

    # Relaciones
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='musico_perfil'
    )
    """
    # Banda

class Evento(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    fecha_evento = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ubicacion = models.CharField(max_length=250)
    # Coordenadas para Google Maps (DecimalField para mayor precisión)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Relaciones
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='eventos_usuario'
    )
    bandas = models.ManyToManyField('Banda', blank=True, related_name='eventos')
    
    def __str__(self):
        return self.titulo

class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    generos_tags = TaggableManager() # Generos
    fecha_creacion = models.DateField()

    # Relaciones
    musicos = models.ManyToManyField(Musico)
    # Los eventos están accesibles a través de banda.eventos.all() (relación inversa de Evento)
    
    def __str__(self):
        return self.nombre

class Anuncio(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    pago = models.FloatField()
    fecha_creacion = models.DateField(default=timezone.now)

    # Relaciones
    bandas = models.ManyToManyField(Banda)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Anuncios'
    )
    
"""
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    cuerpo = models.TextField()
    
    slug = models.SlugField(max_length=250)
    
    autor = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='articulos_blog'
    )
    
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'

    estado = models.CharField(
    max_length=1,
    choices=Estado.choices,
    default=Estado.BORRADOR
    )

    # Define algunos metadatos del modelo, ayudando a gestionar algunas opciones para interactuar con el
    class Meta:
        ordering = ['-publicado'] # Orden descendente (más nuevos primero)
        indexes = [
        models.Index(fields=['-publicado']), # Índice para optimizar consultas
        ]

        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    
    def __str__(self):
        return self.titulo
"""