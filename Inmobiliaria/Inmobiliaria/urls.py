from django.contrib import admin
from django.urls import path, include
from . import views
from usuarios import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("", include("usuarios.urls")),
]
