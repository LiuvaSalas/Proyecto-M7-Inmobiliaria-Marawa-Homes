def detalle_ciudades(request):
    inmuebles_disponibles = Inmueble.objects.filter(arrendada=False)
    inmuebles_destacados = Inmueble.objects.filter(arrendada=False).order_by('-m2_construidos')[:3]
    cuenta_inmuebles_la_serena = (Inmueble.objects.filter(arrendada=False, comuna = 29).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_vina = (Inmueble.objects.filter(arrendada=False, comuna = 41).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_arica = (Inmueble.objects.filter(arrendada=False, comuna = 2).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_santiago = (Inmueble.objects.filter(arrendada=False, comuna = 51).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    cuenta_inmuebles_concepcion = (Inmueble.objects.filter(arrendada=False, comuna = 77).values('comuna__nombre').annotate(total = Count('id')).order_by('-total'))
    contexto = {"inmuebles_disponibles": inmuebles_disponibles, "inmuebles_destacados":inmuebles_destacados, "cuenta_inmuebles_la_serena":cuenta_inmuebles_la_serena,"cuenta_inmuebles_vina":cuenta_inmuebles_vina,"cuenta_inmuebles_arica":cuenta_inmuebles_arica,"cuenta_inmuebles_santiago":cuenta_inmuebles_santiago,"cuenta_inmuebles_concepcion":cuenta_inmuebles_concepcion}
    return contexto