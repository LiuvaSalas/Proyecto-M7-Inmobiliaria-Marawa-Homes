# Generated by Django 5.1.3 on 2024-11-20 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0005_alter_inmueble_arrendador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion_Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_inmueble', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='tipo_inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.clasificacion_inmueble'),
        ),
    ]
