import os
from .base import *

DEBUG = False # Seguridad obligatoria en producción
ALLOWED_HOSTS = ['*'] # En un entorno real, aquí iría el dominio (ej. 'midominio.com')

# Configuración de PostgreSQL leyendo del SO (Inyectado por Docker)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB_CATALOGOMUSICOS'),
        'USER': os.getenv('POSTGRES_USER_CATALOGOMUSICOS'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD_CATALOGOMUSICOS'),
        'HOST': os.getenv('POSTGRES_HOST_CATALOGOMUSICOS', 'db-catalogomusicos'),
        'PORT': os.getenv('POSTGRES_PORT_CATALOGOMUSICOS', '5432'),
    }
}

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
