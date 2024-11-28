from django.contrib import admin
from django.urls import path, include
from . import views
from usuarios import urls
from gestion_inmuebles import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("all_inmuebles/", views.all_inmuebles, name = "all_inmuebles"),
    path("region_metropolitana/", views.inmuebles_region_metropolitana, name = "region_metropolitana"),
    path("los_lagos/", views.inmuebles_los_lagos, name = "los_lagos"),
    path("valparaiso/", views.inmuebles_valparaiso, name = "valparaiso"),
    path("", include("usuarios.urls")),
    path("", include("gestion_inmuebles.urls")),
]
