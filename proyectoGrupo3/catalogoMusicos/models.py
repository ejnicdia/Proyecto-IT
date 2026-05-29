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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Reportes"
    )

    def __str__(self):
        return self.titulo


class Musico(User):
    instrumento = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    fecha_inicio_estudio = models.DateField()


class Evento(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    fecha_evento = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ubicacion = models.CharField(max_length=250)
    # Coordenadas para Google Maps (DecimalField para mayor precisión)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    # Relaciones
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="eventos_usuario",
    )
    bandas = models.ManyToManyField("Banda", blank=True, related_name="eventos")

    def __str__(self):
        return self.titulo


class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_creacion = models.DateField()

    # Relaciones
    musicos = models.ManyToManyField(Musico)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bandas",
        null=True,
        blank=True,
    )

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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Anuncios"
    )
