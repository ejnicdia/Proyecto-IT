# Fixtures - Datos de Prueba

Este directorio contiene archivos de fixtures (datos de prueba) para el proyecto.

## Archivos

- **data.json**: Archivo principal con todos los datos de prueba
  - 1 admin
  - 4 músicos
  - 3 eventos
  - 3 bandas
  - 3 anuncios
  - 3 reportes

## Cómo Usar las Fixtures

### Cargar desde línea de comandos

```bash
# Cargar TODAS las fixtures
python.exe manage.py loaddata data
```

```bash
# Con verbosidad para ver qué se carga
python.exe manage.py loaddata data --verbosity=2
```

```bash
# Cargar y limpiar BD primero
python.exe manage.py flush --noinput && python.exe manage.py loaddata data
```

### Cargar/Descargar Modelos Específicos

#### Descargar (Exportar) Modelos Individuales

```bash
# Exportar usuarios
python.exe manage.py dumpdata auth.user --indent 2 > catalogoMusicos\fixtures\usuarios.json

# Exportar músicos
python.exe manage.py dumpdata catalogoMusicos.Musico --indent 2 > catalogoMusicos\fixtures\musicos.json

# Exportar bandas
python.exe manage.py dumpdata catalogoMusicos.Banda --indent 2 > catalogoMusicos\fixtures\bandas.json

# Exportar eventos
python.exe manage.py dumpdata catalogoMusicos.Evento --indent 2 > catalogoMusicos\fixtures\eventos.json

# Exportar anuncios
python.exe manage.py dumpdata catalogoMusicos.Anuncio --indent 2 > catalogoMusicos\fixtures\anuncios.json

# Exportar reportes
python.exe manage.py dumpdata catalogoMusicos.Reporte --indent 2 > catalogoMusicos\fixtures\reportes.json
```

#### Cargar Modelos Individuales

```bash
# Cargar solo usuarios
python.exe manage.py loaddata usuarios

# Cargar solo músicos
python.exe manage.py loaddata musicos

# Cargar solo bandas
python.exe manage.py loaddata bandas

# Cargar solo eventos
python.exe manage.py loaddata eventos

# Cargar solo anuncios
python.exe manage.py loaddata anuncios

# Cargar solo reportes
python.exe manage.py loaddata reportes
```

#### Cargar Múltiples Modelos en Orden

```bash
# Cargar usuarios y músicos (necesarios para las relaciones)
python.exe manage.py loaddata usuarios musicos

# Cargar con eventos y bandas
python.exe manage.py loaddata usuarios musicos eventos bandas

# Cargar todo excepto reportes
python.exe manage.py loaddata usuarios musicos eventos bandas anuncios
```

## Datos Incluidos

### Usuarios (6 total)

- `admin` (superuser)
- `carlos_guitarra` (Músico - Guitarra)
- `maria_bateria` (Músico - Batería)
- `juan_bajo` (Músico - Bajo)
- `ana_teclados` (Músico - Teclados)
- `pedro_productor` (Usuario normal)

### Bandas (3)
1. **Los Rockeros Clásicos** - 3 músicos, 1 evento
2. **Jazz Cool Fusion** - 2 músicos, 2 eventos
3. **Metal Extreme** - 2 músicos, 1 evento

### Eventos (3)
1. Festival de Rock 2024
2. Concierto Jazz en vivo
3. Jam Session Semanal

### Anuncios (3)
1. Buscamos guitarrista
2. Músicos para grabación
3. Tecladista para tour

### Reportes (3)
1. Error al cargar banda
2. Problema con registro
3. Evento duplicado

## Notas Importantes

1. **Contraseñas Funcionales**: Las contraseñas están correctamente hasheadas y son funcionales:
   - Cada usuario puede iniciar sesión con: `username = contraseña`
   - Ejemplo: `admin` / `admin`, `carlos_guitarra` / `carlos_guitarra`, etc.

2. **TaggableManager**: Los géneros de las bandas no están incluidos en las fixtures JSON (limitación de Django). Deberás agregarlos manualmente si los necesitas:

   ```bash
   python manage.py shell
   
   >>> from catalogoMusicos.models import Banda
   >>> banda = Banda.objects.get(id=1)
   >>> banda.generos_tags.add("rock", "metal")
   ```

3. **Cambiar Contraseñas**: Si necesitas cambiar contraseñas después:

   ```bash
   python manage.py changepassword admin
   ```

4. **Reset de BD**: Para empezar de cero:

   ```bash
   python manage.py flush --noinput  # Borra todo
   python manage.py migrate           # Recrea estructura
   python manage.py loaddata data     # Carga fixtures
   ```

## Exportar Datos Actuales a Fixture

Si tienes datos en tu BD y quieres crear una nueva fixture:

```bash
# Exportar todo
python manage.py dumpdata > data_nueva.json
```

```bash
# Exportar solo de la app
python manage.py dumpdata catalogoMusicos > data_nueva.json
```

```bash
# Exportar con indentación (más legible)
python manage.py dumpdata catalogoMusicos --indent 2 > data_nueva.json
```

## Verificar que se Cargaron Correctamente

```bash
python manage.py shell

>>> from catalogoMusicos.models import Musico, Banda, Evento, Anuncio, Reporte
>>> Musico.objects.count()
4
>>> Banda.objects.count()
3
>>> Evento.objects.count()
3
>>> Anuncio.objects.count()
3
>>> Reporte.objects.count()
3
```
