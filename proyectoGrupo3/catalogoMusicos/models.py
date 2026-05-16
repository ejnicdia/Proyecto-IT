from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

class Banda(models.Model):
    nombre = models.CharField(max_length=250)

    class Genero(models.TextChoices):
        ROCK = 'R', 'Rock'
        POP = 'P', 'Pop'

    genero = models.CharField(
        max_length=1,
        choices=Genero.choices,
        default=Genero.ROCK
    )
    
    fecha_creacion = models.DateField()
    
class Reporte(models.Model):
    
    titulo = models.CharField(max_length=250)
    descripcion_error = models.TextField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Anuncio(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    pago = models.FloatField()
    fecha_creacion = models.DateField(default=timezone.now)
    
class Musico(Usuario):
    
    instrumento = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    fecha_inicio_estudio = models.DateField(auto_now=True)
    
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