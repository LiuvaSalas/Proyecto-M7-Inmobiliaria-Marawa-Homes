# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.log_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path(
        "modificar_perfil/<str:username>/",
        views.modificar_perfil,
        name="modificar_perfil",
    ),
    path(
        "perfil_usuario/<str:username>/",
        views.perfil_usuario,
        name="perfil_usuario",
    ),
]
