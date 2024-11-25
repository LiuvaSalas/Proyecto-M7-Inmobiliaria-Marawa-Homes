def is_arrendador(request):
    if request.user.is_authenticated:
        return {'is_arrendador': request.user.groups.filter(name="arrendador").exists()}
    return {'is_arrendador': False}