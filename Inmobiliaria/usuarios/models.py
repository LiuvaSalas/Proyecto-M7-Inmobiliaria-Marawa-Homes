from django.db import models
from django.contrib.auth.models import User, Group


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, blank=False, null=False)
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=300, blank=False, null=False)
    telefono_personal = models.IntegerField(blank=False, null=False)
    correo_electronico = models.EmailField()
    tipo_de_usuario = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        # return f"{self.nombres} {self.apellidos}"
        return self.user.username
