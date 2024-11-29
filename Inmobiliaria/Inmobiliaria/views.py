from django.shortcuts import redirect, render
from gestion_inmuebles.models import Inmueble
from django.db.models import Q
from django.db.models import Count


def index(request):
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    inmuebles_destacados = Inmueble.objects.filter(arrendada=False).order_by(
        "precio_mensual"
    )[:3]

    contexto = {
        "inmuebles_disponibles": inmuebles_disponibles,
        "inmuebles_destacados": inmuebles_destacados,
    }
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html")


def all_inmuebles(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    if queryset:
        inmuebles_disponibles = Inmueble.objects.filter(
            Q(comuna__nombre__icontains=queryset)
            | Q(descripcion__icontains=queryset)
            | Q(region__nombre__icontains=queryset)
            | Q(tipo_inmueble__tipo_de_inmueble__icontains=queryset)
            | Q(region__identificador__icontains=queryset),
            arrendada=False,
        ).distinct()
        respuesta = inmuebles_disponibles.exists()
    else:
        respuesta = inmuebles_disponibles.exists()
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "respuesta": respuesta}
    return render(request, "all_inmuebles.html", contexto)


def inmuebles_region_metropolitana(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False, region=8)
    if queryset:
        inmuebles_disponibles = Inmueble.objects.filter(
            Q(comuna__nombre__icontains=queryset) | Q(descripcion__icontains=queryset),
            arrendada=False,
            region=8,
        ).distinct()
        respuesta = inmuebles_disponibles.exists()
    else:
        respuesta = inmuebles_disponibles.exists()
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "respuesta": respuesta}
    return render(request, "region_metropolitana.html", contexto)


def inmuebles_los_lagos(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False, region=14)
    if queryset:
        inmuebles_disponibles = Inmueble.objects.filter(
            Q(comuna__nombre__icontains=queryset) | Q(descripcion__icontains=queryset),
            arrendada=False,
            region=8,
        ).distinct()
        respuesta = inmuebles_disponibles.exists()
    else:
        respuesta = inmuebles_disponibles.exists()
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "respuesta": respuesta}
    return render(request, "los_lagos.html", contexto)


def inmuebles_valparaiso(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False, region=7)
    if queryset:
        inmuebles_disponibles = Inmueble.objects.filter(
            Q(comuna__nombre__icontains=queryset) | Q(descripcion__icontains=queryset),
            arrendada=False,
            region=8,
        ).distinct()
        respuesta = inmuebles_disponibles.exists()
    else:
        respuesta = inmuebles_disponibles.exists()
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "respuesta": respuesta}
    return render(request, "valparaiso.html", contexto)
