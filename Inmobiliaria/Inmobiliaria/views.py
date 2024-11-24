from django.shortcuts import redirect, render
from gestion_inmuebles.models import Inmueble
from django.db.models import Q
from django.db.models import Count


def index(request):
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    inmuebles_destacados = Inmueble.objects.filter(arrendada=False).order_by('-m2_construidos')[:3]
    cuenta_inmuebles_la_serena = (Inmueble.objects.filter(arrendada=False, comuna = 29).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_vina = (Inmueble.objects.filter(arrendada=False, comuna = 41).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_arica = (Inmueble.objects.filter(arrendada=False, comuna = 2).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_santiago = (Inmueble.objects.filter(arrendada=False, comuna = 51).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_concepcion = (Inmueble.objects.filter(arrendada=False, comuna = 77).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    print(cuenta_inmuebles_santiago)
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "inmuebles_destacados":inmuebles_destacados, "cuenta_inmuebles_la_serena":cuenta_inmuebles_la_serena,"cuenta_inmuebles_vina":cuenta_inmuebles_vina,"cuenta_inmuebles_arica":cuenta_inmuebles_arica,"cuenta_inmuebles_santiago":cuenta_inmuebles_santiago,"cuenta_inmuebles_concepcion":cuenta_inmuebles_concepcion}
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


