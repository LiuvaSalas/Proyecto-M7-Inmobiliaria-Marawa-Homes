import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Inmueble
from .forms import Formulario_Actualizacion_Inmuebles, Formulario_Gestion_Inmuebles


def home(request):
    return render(request, "home.html")


@login_required
def listar_inmuebles(request):
    inmuebles_general = Inmueble.objects.filter(arrendador__user=request.user)
    contexto = {"inmuebles_general": inmuebles_general}
    return render(request, "inmuebles/listar_inmuebles.html", contexto)


def crear_inmueble(request):
    if request.method == "GET":
        return render(
            request,
            "inmuebles/crear_inmueble.html",
            {"form": Formulario_Gestion_Inmuebles()},
        )
    else:
        try:
            if request.method == "POST":
                form = Formulario_Gestion_Inmuebles(request.POST)
                if form.is_valid():
                    nuevo_inmueble = form.save(commit=False)
                    nuevo_inmueble.arrendador = request.user.usuario
                    nuevo_inmueble.save()
                    return redirect("listar_inmuebles")
            else:
                form = Formulario_Gestion_Inmuebles()
                return render(request, "inmuebles/crear_inmueble.html", {"form": form})
        except ValueError:
            return render(
                request,
                "inmuebles/crear_inmueble.html",
                {
                    "form": form,
                    "error": "Ingresa datos válidos en el inmueble",
                },
            )


def detalle_inmueble(request, inmueble_id):
    if request.method == "GET":
        inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
        form = Formulario_Actualizacion_Inmuebles(instance=inmueble)
        return render(
            request,
            "inmuebles/detalle_inmueble.html",
            {"inmueble": inmueble, "form": form},
        )
    else:
        try:
            inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
            form = Formulario_Actualizacion_Inmuebles(request.POST, instance=inmueble)
            form.save()
            return redirect("listar_inmuebles")
        except:
            return render(
                request,
                "inmuebles/detalle_inmueble.html",
                {
                    "inmueble": inmueble,
                    "form": form,
                    "error": "Se ha generado un error actualizando el inmueble",
                },
            )


def borrar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    inmueble.delete()
    return redirect("listar_inmuebles")


def dashboard(request):
    inmuebles_general = Inmueble.objects.filter(arrendador__user=request.user)
    total_inmuebles = inmuebles_general.count()
    inmuebles_arrendados = inmuebles_general.filter(arrendada=True).count()
    inmuebles_sin_arrendar = total_inmuebles - inmuebles_arrendados

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    ax.bar(
        ["Arrendados", "Sin Arrendar"],
        [inmuebles_arrendados, inmuebles_sin_arrendar],
        color=["blue", "orange"],
    )
    ax.set_title("Inmuebles Arrendados vs Sin Arrendar")
    ax.set_ylabel("Cantidad")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    contexto = {
        "inmuebles_general": inmuebles_general,
        "total_inmuebles": total_inmuebles,
        "inmuebles_arrendados": inmuebles_arrendados,
        "inmuebles_sin_arrendar": inmuebles_sin_arrendar,
        "graph_inmuebles": image_base64,
    }

    return render(request, "inmuebles/dashboard.html", contexto)
