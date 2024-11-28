from django.forms import ModelForm
from .models import Inmueble, ContactForm
from django import forms


class Formulario_Gestion_Inmuebles(ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "m2_construidos",
            "m2_totales",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "region",
            "comuna",
            "tipo_inmueble",
            "precio_mensual",
            "imagen_portada",
            'imagen1',
            'imagen2',
            'imagen3',
            'imagen4',
            'imagen5',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del inmueble'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción del inmueble'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Metros cuadrados construidos'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Metros cuadrados totales'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de estacionamientos'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de habitaciones'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de baños'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del inmueble'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio mensual'}),
            'imagen_portada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portada del Inmueble'}),
            'imagen1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 1'}),
            'imagen2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 2'}),
            'imagen3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 3'}),
            'imagen4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 4'}),
            'imagen5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 5'}),
        }


class Formulario_Actualizacion_Inmuebles(ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "m2_construidos",
            "m2_totales",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "region",
            "comuna",
            "tipo_inmueble",
            "precio_mensual",
            "imagen_portada",
            'imagen1',
            'imagen2',
            'imagen3',
            'imagen4',
            'imagen5',
            "arrendada",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del inmueble'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción del inmueble'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Metros cuadrados construidos'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Metros cuadrados totales'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de estacionamientos'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de habitaciones'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de baños'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del inmueble'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio mensual'}),
            'imagen_portada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portada del Inmueble'}),
            'imagen1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 1'}),
            'imagen2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 2'}),
            'imagen3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 3'}),
            'imagen4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 4'}),
            'imagen5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagen 5'}),
            'arrendada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={"class": "form-control custom-input"}),
    )
    customer_name = forms.CharField(
        max_length=64,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control custom-input"}),
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={"class": "form-control custom-textarea", "rows": 5}
        ),
    )
