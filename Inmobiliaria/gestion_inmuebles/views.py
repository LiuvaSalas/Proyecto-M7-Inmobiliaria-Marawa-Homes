import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Inmueble, ContactForm
from .forms import (
    Formulario_Actualizacion_Inmuebles,
    Formulario_Gestion_Inmuebles,
    ContactFormForm,
)
from Inmobiliaria.views import index
from django.http import HttpResponseRedirect
from django.db.models import Avg


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


def caracteristica_inmueble(request, inmueble_id):
    if request.method == "GET":
        inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
        contexto = {"inmueble": inmueble}
        return render(
            request,
            "inmuebles/caracteristica_inmueble.html",
            contexto,
        )
    else:
        redirect("index")


def dashboard(request):
    inmuebles_general = Inmueble.objects.filter(arrendador__user=request.user)
    total_inmuebles = inmuebles_general.count()
    inmuebles_arrendados = inmuebles_general.filter(arrendada=True).count()
    inmuebles_sin_arrendar = total_inmuebles - inmuebles_arrendados
    promedio_precio_inmuebles = round(inmuebles_general.aggregate(Avg('precio_mensual'))['precio_mensual__avg'] or 0)
    inmuebles_parcela = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble = "Parcela").count()
    inmuebles_casa = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble = "Casa").count()
    inmuebles_departamento = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble = "Departamento").count()
    promedio_precio_parcela = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble="Parcela").aggregate(Avg('precio_mensual'))['precio_mensual__avg'] or 0
    promedio_precio_casa = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble="Casa").aggregate(Avg('precio_mensual'))['precio_mensual__avg'] or 0
    promedio_precio_departamento = inmuebles_general.filter(tipo_inmueble__tipo_de_inmueble="Departamento").aggregate(Avg('precio_mensual'))['precio_mensual__avg'] or 0

    # Imuebles arrendados/Inmuebles sin arrendar
    fig1, ax1 = plt.subplots(1, 1, figsize=(8, 6))
    bars1 = ax1.bar(
        ["Arrendados", "Sin Arrendar"],
        [inmuebles_arrendados, inmuebles_sin_arrendar],
        color=["#85A98F", "#525B44"],
    )
    ax1.set_title("Inmuebles Arrendados vs Sin Arrendar")
    ax1.set_ylabel("Cantidad")

    # Añadir etiquetas a cada barra
    ax1.bar_label(bars1, padding=3, fmt='%.0f', fontsize=18)

    buf1 = BytesIO()
    plt.savefig(buf1, format="png")
    buf1.seek(0)
    graph1_base64 = base64.b64encode(buf1.getvalue()).decode("utf-8")
    buf1.close()

    # Imuebles por tipo de inmueble
    fig2, ax2 = plt.subplots(1, 1, figsize=(8, 6))
    bars2 = ax2.bar(
        ["Parcela", "Casa", "Departamento"],
        [inmuebles_parcela, inmuebles_casa, inmuebles_departamento],
        color=["#355F2E", "#F4E0AF", "#F9C0AB"],
    )
    ax2.set_title("Número de Inmuebles por Tipo")
    ax2.set_ylabel("Cantidad")

    # Añadir etiquetas a cada barra
    ax2.bar_label(bars2, padding=3, fmt='%.0f', fontsize=18)

    buf2 = BytesIO()
    plt.savefig(buf2, format="png")
    buf2.seek(0)
    graph2_base64 = base64.b64encode(buf2.getvalue()).decode("utf-8")
    buf2.close()

    # Precio por tipo de inmueble
    fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))
    ax3.bar(
        ["Parcela", "Casa", "Departamento"],
        [promedio_precio_parcela, promedio_precio_casa, promedio_precio_departamento],
        color=["#355F2E", "#F4E0AF", "#F9C0AB"],
    )
    ax3.set_title("Precio Promedio por Tipo")
    ax3.set_ylabel("Precio")

    buf3 = BytesIO()
    plt.savefig(buf3, format="png")
    buf3.seek(0)
    graph3_base64 = base64.b64encode(buf3.getvalue()).decode("utf-8")
    buf3.close()

    contexto = {
        "inmuebles_general": inmuebles_general,
        "total_inmuebles": total_inmuebles,
        "inmuebles_arrendados": inmuebles_arrendados,
        "inmuebles_sin_arrendar": inmuebles_sin_arrendar,
        "graph_inmuebles": graph1_base64,
        "graph_tipo_inmuebles": graph2_base64,
        "graph_precio_tipo_inmuebles": graph3_base64,
        "promedio_precio_inmuebles": promedio_precio_inmuebles,
    }

    return render(request, "inmuebles/dashboard.html", contexto)


def envio_exitoso(request):
    return render(request, "envio_exitoso.html", {})


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/envio_exitoso")
    else:
        form = ContactFormForm()

    return render(request, "contacto.html", {"form": form})
