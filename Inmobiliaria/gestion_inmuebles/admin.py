from django.contrib import admin
from .models import Inmueble, Region, Comuna, Clasificacion_Inmueble
from django.utils import timezone


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "precio_mensual")
    search_fields = ("nombre", "direccion", "tipo_inmueble__tipo_inmueble")
    list_filter = ("precio_mensual", "region__nombre")
    readonly_fields = ("fecha_creacion", "ultima_modificacion")

    def save_model(self, request, obj, form, change):
        if change:
            obj.ultima_modificacion = timezone.now()
        else:
            obj.fecha_creacion = timezone.now()
            obj.save()


admin.site.register(Region)


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "get_region")
    search_fields = ("region__nombre", "nombre")


admin.site.register(Clasificacion_Inmueble)
