import os
import django
import random
from datetime import timedelta, date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoMusica.settings')
django.setup()

from django.contrib.auth import get_user_model
from catalogoMusicos.models import Musico

# Lista de instrumentos para generar datos realistas
INSTRUMENTOS = [
    "Guitarra", "Batería", "Bajo", "Piano", "Violín", 
    "Flauta", "Saxofón", "Trompeta", "Teclado", "Violonchelo",
    "Harmónica", "Mandolina", "Arpa", "Timbal", "Maracas"
]

# Biografías de ejemplo
BIOGRAFIAS = [
    "Músico apasionado con experiencia de más de 10 años.",
    "Dedicado a perfeccionar el arte de la música desde la infancia.",
    "Amante de la música clásica y moderna.",
    "Instructor de música con formación académica completa.",
    "Artista versátil que toca múltiples géneros musicales."
]

# 1. Obtenemos el usuario autor (el admin)
User = get_user_model()
usuario = User.objects.first()

if not usuario:
    print("¡Error! No se ha encontrado ningún usuario. Crea un superusuario primero.")
else:
    print(f"Generando músicos con usuario: {usuario.username}...\n")

    # 2. Bucle para crear 15 músicos
    for i in range(1, 16):
        nombre_usuario = f"musico_{i}"
        email = f"musico{i}@example.com"
        instrumento = random.choice(INSTRUMENTOS)
        bio = random.choice(BIOGRAFIAS)
        
        # Generamos una fecha aleatoria en los últimos 3650 días (10 años)
        dias_atras = random.randint(0, 3650)
        fecha_inicio = date.today() - timedelta(days=dias_atras)
        
        musico = Musico.objects.create(
            username=nombre_usuario,
            email=email,
            instrumento=instrumento,
            bio=bio,
            fecha_inicio_estudio=fecha_inicio,
            usuario=usuario
        )
        print(f" -> Creado: {nombre_usuario} - Instrumento: {instrumento}")
    
    print("\n¡Proceso finalizado! 15 músicos creados correctamente.")