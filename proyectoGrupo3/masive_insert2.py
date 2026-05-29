import os
import django
import random
from datetime import timedelta, date
from django.utils import timezone

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoMusica.settings')
django.setup()

from django.contrib.auth import get_user_model
# ¡Ajusta 'catalogoMusicos' al nombre real de tu app donde están los modelos!
from catalogoMusicos.models import Banda, Evento, Anuncio

# --- Datos de Ejemplo para Generación Aleatoria ---

GENEROS = ["Rock", "Pop", "Jazz", "Metal", "Indie", "Blues", "Salsa", "Folk", "Reggae"]
NOMBRES_BANDAS = ["Los Gatos", "Sombras", "Ecos", "Los Soñadores", "Rayo", "Trueno", "Caminantes", "Acordes"]

UBICACIONES = ["Sala Apolo", "Wizink Center", "Teatro Central", "Auditorio Municipal", "Bar El Templo", "Plaza Mayor"]
DESCRIPCIONES_EVENTOS = [
    "Un concierto inolvidable lleno de energía.",
    "Presentación del nuevo disco con invitados especiales.",
    "Música en vivo para disfrutar con amigos.",
    "Festival anual con las mejores bandas de la ciudad."
]

TITULOS_ANUNCIOS = [
    "Buscamos baterista urgente",
    "Se necesita cantante para banda de rock",
    "Banda disponible para bodas y eventos",
    "Compramos amplificadores",
    "Se ofrece guitarrista con experiencia"
]
DESCRIPCIONES_ANUNCIOS = [
    "Imprescindible tener equipo propio y disponibilidad.",
    "Buscamos a alguien comprometido y con ganas de tocar.",
    "Ofrecemos un repertorio variado y adaptado.",
    "Contactar por este medio para más detalles."
]

# 1. Obtenemos el usuario autor
User = get_user_model()
usuario = User.objects.first()

if not usuario:
    print("¡Error! No se ha encontrado ningún usuario. Crea un superusuario primero.")
else:
    print(f"Generando datos con usuario: {usuario.username}...\n")

    # --- 1. Generación de EVENTOS ---
    # Los creamos primero para luego poder asignarlos a las Bandas
    print(">>> Creando Eventos...")
    eventos_creados = []
    for i in range(1, 16):
        titulo = f"Evento Musical {i}"
        
        # Generamos fecha_evento en el futuro
        dias_futuro = random.randint(1, 100)
        horas_futuro = random.randint(10, 23)
        fecha_evento = timezone.now() + timedelta(days=dias_futuro, hours=horas_futuro)
        
        ubicacion = random.choice(UBICACIONES)
        descripcion = random.choice(DESCRIPCIONES_EVENTOS)
        
        # No pasamos fecha_creacion porque tiene auto_now_add=True
        evento = Evento.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha_evento=fecha_evento,
            ubicacion=ubicacion,
            usuario=usuario
        )
        eventos_creados.append(evento)
        print(f" -> Creado Evento: {evento.titulo}")

    # --- 2. Generación de BANDAS ---
    print("\n>>> Creando Bandas...")
    bandas_creadas = []
    for i in range(1, 16):
        nombre_banda = f"{random.choice(NOMBRES_BANDAS)} {i}"
        
        dias_atras = random.randint(0, 1825)
        fecha_creacion = date.today() - timedelta(days=dias_atras)
        
        banda = Banda.objects.create(
            nombre=nombre_banda,
            fecha_creacion=fecha_creacion
        )
        
        # Agregar tags (TaggableManager)
        #tags_elegidos = random.sample(GENEROS, k=random.randint(1, 3))
        #banda.generos_tags.add(*tags_elegidos)
        
        # Asignar entre 1 y 3 eventos aleatorios a la banda (ManyToMany)
        if eventos_creados:
            eventos_asignar = random.sample(eventos_creados, k=random.randint(1, min(3, len(eventos_creados))))
            banda.eventos.set(eventos_asignar)
            
        bandas_creadas.append(banda)
        #print(f" -> Creada Banda: {banda.nombre} (Tags: {', '.join(tags_elegidos)})")

    # --- 3. Generación de ANUNCIOS ---
    print("\n>>> Creando Anuncios...")
    for i in range(1, 16):
        titulo = f"{random.choice(TITULOS_ANUNCIOS)} #{i}"
        descripcion = random.choice(DESCRIPCIONES_ANUNCIOS)
        pago = round(random.uniform(0.0, 500.0), 2)
        
        # Creamos el anuncio
        anuncio = Anuncio.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            pago=pago,
            usuario=usuario
        )
        
        # Asignar entre 1 y 2 bandas aleatorias al anuncio (ManyToMany)
        if bandas_creadas:
            bandas_asignar = random.sample(bandas_creadas, k=random.randint(1, min(2, len(bandas_creadas))))
            anuncio.bandas.set(bandas_asignar)
            
        print(f" -> Creado Anuncio: {anuncio.titulo} (Pago: {anuncio.pago}€)")

    print("\n¡Proceso finalizado! 15 Eventos, 15 Bandas y 15 Anuncios creados correctamente y relacionados entre sí.")