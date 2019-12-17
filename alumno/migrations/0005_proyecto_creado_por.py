# Generated by Django 2.2.6 on 2019-12-16 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumno', '0004_proyecto_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='creado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_proyecto', to=settings.AUTH_USER_MODEL),
        ),
    ]
