from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    
class Reporte(models.Model):
    
    titulo = models.CharField(max_length=250)
    descripcion_error = models.TextField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.titulo