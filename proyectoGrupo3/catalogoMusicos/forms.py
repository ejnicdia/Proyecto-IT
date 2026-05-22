from django import forms
from django.contrib.auth import get_user_model
from .models import Musico, Banda, Anuncio, Reporte, Evento

# UsuarioForm, MusicoForm, BandaForm, AnuncioForm, ReporteForm, EventoForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = []

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = []

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = []

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = []

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = []

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = []

class FormularioRegistro(forms.ModelForm):
    # Aunque ya está en el modelo, hay que indicarle que es un PasswordInput o lo renderizará como texto
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput) # widget para que no se vea la contraseña.
    # Este otro campo será para validar que la contraseña está bien escrita
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    # Campos que se recuperan del modelo User de Django
    class Meta:
        # Coge el que haya por defecto en el sistema. Por si quieres hacer un tipo de usuario tuyo personalizado.
        model = get_user_model()
        fields = ['username', 'last_name', 'email']
        help_texts = {'username': None} # Oculta el texto de ayuda predeterminado de este campo

    def clean_password2(self):
        # self.cleaned_data es un diccionario de Django que contiene todos los datos
        # que se han introducido y que ya han pasado la validación básica
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            # Si los campos de contraseña difieren, se lanza un ValidationError que Django captura
            # automáticamente e implica mostrar ese mensaje de texto en rojo junto al campo en el HTML
            raise forms.ValidationError("Las contraseñas no coinciden.")
        # Si las contraseñas coinciden se devuelve ya validada para que Django siga su proceso normal
        return cd['password2']


"""
class FormularioEmailArticulo(forms.Form):
    nombre = forms.CharField(max_length=60)
    remitente = forms.EmailField()
    destinatario = forms.EmailField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)

# Creamos el formulario del modelo que hemos creado (Comentario)
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo']

class FormularioRegistro(forms.ModelForm):
    # Aunque ya está en el modelo, hay que indicarle que es un PasswordInput o lo renderizará como texto
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput) # widget para que no se vea la contraseña.
    # Este otro campo será para validar que la contraseña está bien escrita
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    # Campos que se recuperan del modelo User de Django
    class Meta:
        # Coge el que haya por defecto en el sistema. Por si quieres hacer un tipo de usuario tuyo personalizado.
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {'username': None} # Oculta el texto de ayuda predeterminado de este campo

    def clean_password2(self):
        # self.cleaned_data es un diccionario de Django que contiene todos los datos
        # que se han introducido y que ya han pasado la validación básica
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            # Si los campos de contraseña difieren, se lanza un ValidationError que Django captura
            # automáticamente e implica mostrar ese mensaje de texto en rojo junto al campo en el HTML
            raise forms.ValidationError("Las contraseñas no coinciden.")
        # Si las contraseñas coinciden se devuelve ya validada para que Django siga su proceso normal
        return cd['password2']

class LibroExternoForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=100)
    isbn = forms.CharField(label="ISBN", max_length=20)
    fecha = forms.DateField(label="Fecha Publicación", widget=forms.TextInput(attrs={'type': 'date'}))
    autor_id = forms.IntegerField(label="ID de Autor (ej: 1)")

"""
