from django.shortcuts import redirect, render
from gestion_inmuebles.models import Inmueble
from django.db.models import Q


def index(request):
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    inmuebles_destacados = Inmueble.objects.filter(arrendada=False).order_by('-m2_construidos')[:3]
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "inmuebles_destacados":inmuebles_destacados}
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html")

def all_inmuebles(request):
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    contexto = {"inmuebles_disponibles": inmuebles_disponibles}
    return render(request, "all_inmuebles.html", contexto)


def inmuebles_region_metropolitana(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False,region = 8)
    if queryset:
        inmuebles_disponibles = Inmueble.objects.filter(Q(comuna__nombre__icontains = queryset)|Q(descripcion__icontains = queryset), arrendada = False, region = 8).distinct()
        respuesta = inmuebles_disponibles.exists()
    else:
        respuesta = inmuebles_disponibles.exists()
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "respuesta":respuesta}
    return render(request, "region_metropolitana.html", contexto)


