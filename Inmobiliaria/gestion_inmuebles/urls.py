# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("listar_inmuebles/", views.listar_inmuebles, name="listar_inmuebles"),
    path("crear_inmueble/", views.crear_inmueble, name="crear_inmueble"),
    path(
        "detalleInmueble/<int:inmueble_id>",
        views.detalle_inmueble,
        name="detalleInmueble",
    ),
    path(
        "borrarInmueble/<int:inmueble_id>",
        views.borrar_inmueble,
        name="borrarInmueble",
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "caracteristica_inmueble/<int:inmueble_id>",
        views.caracteristica_inmueble,
        name="caracteristica_inmueble",
    ),
]
