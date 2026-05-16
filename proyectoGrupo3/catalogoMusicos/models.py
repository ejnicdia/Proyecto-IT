from django.conf import settings
from django.db import models
from django.utils import timezone


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


class Usuario(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    
class Reporte(models.Model):
    
    titulo = models.CharField(max_length=250)
    descripcion_error = models.TextField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.titulo
    
class Musico(Usuario):
    
    instrumento = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    fecha_inicio_estudio = models.DateField(auto_now=True)