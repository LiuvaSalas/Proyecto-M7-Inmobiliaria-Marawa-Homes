from django.db import models
from usuarios.models import Usuario


class Region(models.Model):
    identificador = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_region(self):
        return self.region.nombre


class Clasificacion_Inmueble(models.Model):
    tipo_de_inmueble = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_de_inmueble


class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(Clasificacion_Inmueble, on_delete=models.CASCADE)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    arrendada = models.BooleanField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
