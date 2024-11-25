from django.forms import ModelForm
from .models import Inmueble


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
        ]


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
            "arrendada",
        ]
