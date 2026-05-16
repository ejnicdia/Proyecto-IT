from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=250)

"""
class Articulo(models.Model):
    # Campos para título y cuerpo
    titulo = models.CharField(max_length=250)
    cuerpo = models.TextField()

    # Campo para la URL amigable (ej: titulo-del-articulo)
    slug = models.SlugField(max_length=250)

    # Relación con el Autor (Usuario)
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

    class Meta:
        ordering = ['-publicado'] # Orden descendente (más nuevos primero)
        indexes = [
        models.Index(fields=['-publicado']), # Índice para optimizar consultas
        ]
        # Opcional: Nombres legibles en el panel de administracion
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.titulo
"""