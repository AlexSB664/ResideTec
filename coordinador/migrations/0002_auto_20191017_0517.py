# Generated by Django 2.2 on 2019-10-17 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superusuario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coordinador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinador',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrera_administra', to='superusuario.Carrera'),
        ),
        migrations.AddField(
            model_name='coordinador',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]