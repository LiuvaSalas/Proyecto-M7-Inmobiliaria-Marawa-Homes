# Generated by Django 5.1.3 on 2024-11-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0010_inmueble_imagen_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='imagen_portada',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]