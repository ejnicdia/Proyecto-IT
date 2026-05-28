/**
 * Script para manejar la selección de ubicación en Google Maps para eventos
 * Permite seleccionar coordenadas mediante un mapa interactivo
 */

let eventMap;
let eventMarker;
let mapInitialized = false;

/**
 * Espera a que Google Maps esté cargado y luego inicializa el mapa
 */
function waitForGoogleMaps() {
    if (typeof google !== 'undefined' && google.maps) {
        // Google Maps está cargado, inicializar el mapa
        console.log('Google Maps API cargada, iniciando mapa...');
        initEventMap();
        mapInitialized = true;
    } else {
        // Reintentar en 100ms
        console.log('Esperando a que Google Maps se cargue...');
        setTimeout(waitForGoogleMaps, 100);
    }
}

/**
 * Inicializa el mapa para seleccionar ubicación de evento
 */
function initEventMap() {
    // Obtener el contenedor del mapa
    const mapContainer = document.getElementById('map-event');
    
    // Si no existe el contenedor, retornar
    if (!mapContainer) {
        console.error('No se encontró el contenedor del mapa con id="map-event"');
        return;
    }

    // Obtener los inputs del formulario
    const latitudeInput = document.getElementById('id_latitud');
    const longitudeInput = document.getElementById('id_longitud');
    const ubicacionInput = document.getElementById('id_ubicacion');
    
    // Si no existen los inputs, no hacer nada
    if (!latitudeInput || !longitudeInput) {
        console.error('No se encontraron los inputs de latitud/longitud');
        return;
    }

    // Coordenadas por defecto (Madrid, España)
    const defaultLat = latitudeInput.value ? parseFloat(latitudeInput.value) : 40.4168;
    const defaultLng = longitudeInput.value ? parseFloat(longitudeInput.value) : -3.7038;
    const defaultCenter = { lat: defaultLat, lng: defaultLng };

    // Crear el mapa
    try {
        eventMap = new google.maps.Map(mapContainer, {
            zoom: 12,
            center: defaultCenter,
            mapTypeControl: true,
            fullscreenControl: true
        });
        
        console.log('Mapa inicializado correctamente');
    } catch (error) {
        console.error('Error al inicializar Google Maps:', error);
        return;
    }

    // Crear marcador si ya hay coordenadas
    if (latitudeInput.value && longitudeInput.value) {
        eventMarker = new google.maps.Marker({
            position: defaultCenter,
            map: eventMap,
            draggable: true,
            title: 'Ubicación del evento'
        });

        eventMarker.addListener('dragend', function() {
            const position = eventMarker.getPosition();
            latitudeInput.value = position.lat().toFixed(6);
            longitudeInput.value = position.lng().toFixed(6);
            updateLocationPreview();
        });
    }

    // Agregar listener al mapa para hacer clic
    eventMap.addListener('click', function(e) {
        const clickedLocation = e.latLng;
        
        // Si ya existe un marcador, eliminarlo
        if (eventMarker) {
            eventMarker.setMap(null);
        }

        // Crear nuevo marcador
        eventMarker = new google.maps.Marker({
            position: clickedLocation,
            map: eventMap,
            draggable: true,
            title: 'Ubicación del evento'
        });

        // Actualizar los campos de entrada
        latitudeInput.value = clickedLocation.lat().toFixed(6);
        longitudeInput.value = clickedLocation.lng().toFixed(6);

        // Agregar listener al marcador para permitir arrastrarlo
        eventMarker.addListener('dragend', function() {
            const position = eventMarker.getPosition();
            latitudeInput.value = position.lat().toFixed(6);
            longitudeInput.value = position.lng().toFixed(6);
            updateLocationPreview();
        });

        // Geococodificar para obtener el nombre de la ubicación
        geocodeLocation(clickedLocation);
        updateLocationPreview();
    });

    // Agregar búsqueda de lugares
    addPlacesSearch();
}

/**
 * Geococodifica una ubicación para obtener su nombre
 */
function geocodeLocation(location) {
    const geocoder = new google.maps.Geocoder();
    
    geocoder.geocode({ location: location }, function(results, status) {
        if (status === 'OK' && results.length > 0) {
            const ubicacionInput = document.getElementById('id_ubicacion');
            if (ubicacionInput) {
                // Usar la dirección más específica disponible
                ubicacionInput.value = results[0].formatted_address;
            }
        } else {
            console.log('Geocoder status:', status);
        }
    });
}

/**
 * Actualiza la vista previa de la ubicación seleccionada
 */
function updateLocationPreview() {
    const latitudeInput = document.getElementById('id_latitud');
    const longitudeInput = document.getElementById('id_longitud');
    
    if (latitudeInput.value && longitudeInput.value) {
        const previewText = `Ubicación seleccionada: ${latitudeInput.value}, ${longitudeInput.value}`;
        let previewElement = document.getElementById('location-preview');
        
        if (!previewElement) {
            previewElement = document.createElement('div');
            previewElement.id = 'location-preview';
            previewElement.style.cssText = `
                padding: 8px;
                background-color: #f0f7ff;
                border-left: 4px solid #1976d2;
                margin: 10px 0;
                font-size: 0.9em;
            `;
            const latitudeInput = document.getElementById('id_latitud');
            latitudeInput.parentNode.appendChild(previewElement);
        }
        
        previewElement.textContent = previewText;
    }
}

/**
 * Agrega funcionalidad de búsqueda de lugares al campo de ubicación del formulario
 */
function addPlacesSearch() {
    // Obtener el campo de ubicación existente en el formulario
    const ubicacionInput = document.getElementById('id_ubicacion');
    
    if (!ubicacionInput || !eventMap) {
        console.error('No se puede agregar búsqueda de lugares: falta campo de ubicación o mapa');
        return;
    }

    // Crear servicio de autocomplete vinculado al campo existente
    const autocomplete = new google.maps.places.Autocomplete(ubicacionInput, {
        types: ['geocode']
    });

    autocomplete.bindTo('bounds', eventMap);

    autocomplete.addListener('place_changed', function() {
        const place = autocomplete.getPlace();
        
        if (!place.geometry) {
            console.warn('No se encontró ubicación para:', place.name);
            return;
        }

        // Centrar el mapa en la ubicación encontrada
        if (place.geometry.viewport) {
            eventMap.fitBounds(place.geometry.viewport);
        } else {
            eventMap.setCenter(place.geometry.location);
            eventMap.setZoom(15);
        }

        // Eliminar marcador anterior
        if (eventMarker) {
            eventMarker.setMap(null);
        }

        // Crear nuevo marcador
        eventMarker = new google.maps.Marker({
            position: place.geometry.location,
            map: eventMap,
            draggable: true,
            title: place.name
        });

        // Actualizar inputs
        const latitudeInput = document.getElementById('id_latitud');
        const longitudeInput = document.getElementById('id_longitud');

        latitudeInput.value = place.geometry.location.lat().toFixed(6);
        longitudeInput.value = place.geometry.location.lng().toFixed(6);
        ubicacionInput.value = place.formatted_address;

        // Agregar listener al marcador
        eventMarker.addListener('dragend', function() {
            const position = eventMarker.getPosition();
            latitudeInput.value = position.lat().toFixed(6);
            longitudeInput.value = position.lng().toFixed(6);
            geocodeLocation(position);
        });

        updateLocationPreview();
    });
}

/**
 * Inicia el proceso de espera cuando el documento esté listo
 */
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', waitForGoogleMaps);
} else {
    // Si el documento ya está cargado, esperar a Google Maps
    waitForGoogleMaps();
}
