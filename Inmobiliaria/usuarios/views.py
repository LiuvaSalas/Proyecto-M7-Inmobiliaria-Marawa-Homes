from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from Inmobiliaria.views import index
from .forms import RegistroUsuarioForm
from django.contrib import messages
from .models import Usuario


# Registro de usuario
def sign_up(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("index")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = RegistroUsuarioForm()

    return render(request, "signup.html", {"form": form})


# Cierre de sesion
def sign_out(request):
    logout(request)
    # return redirect("index")
    return render(request, "logout.html")


# Inicio de sesion
def log_in(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "El usuario o contraseñas son incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("index")

@login_required
def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(Usuario, user=usuario)

    return render(
        request,
        "perfil_usuario.html",
        {"usuario": usuario, "perfil_usuario": perfil_usuario},
    )

@login_required
def modificar_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(Usuario, user=usuario)
    if request.method == "POST":
        nueva_direccion = request.POST.get("nueva_direccion")
        nuevo_telefono_personal = request.POST.get("nuevo_telefono_personal")
        nuevo_correo_electronico = request.POST.get("nuevo_correo_electronico")
        perfil_usuario.direccion = nueva_direccion
        perfil_usuario.telefono_personal = nuevo_telefono_personal
        perfil_usuario.correo_electronico = nuevo_correo_electronico
        perfil_usuario.save()
    return render(
        request,
        "modificar_perfil.html",
        {"usuario": usuario, "perfil_usuario": perfil_usuario},
    )

