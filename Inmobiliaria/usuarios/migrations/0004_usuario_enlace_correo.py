# Generated by Django 5.1.3 on 2024-11-28 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_enlace_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='enlace_correo',
            field=models.CharField(blank=True, default=None, null=True),
        ),
    ]