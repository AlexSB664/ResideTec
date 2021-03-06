# Generated by Django 3.0 on 2019-12-05 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superusuario', '0001_initial'),
        ('asesor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='asesorinterno',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrera_del_asesorinterno', to='superusuario.Carrera'),
        ),
        migrations.AddField(
            model_name='asesorinterno',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asesorinterno',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodo_del_asesorinterno', to='superusuario.Periodo'),
        ),
        migrations.AddField(
            model_name='asesorexterno',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrera_del_asesorexterno', to='superusuario.Carrera'),
        ),
        migrations.AddField(
            model_name='asesorexterno',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asesorexterno',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_del_asesorexterno', to='superusuario.Empresa'),
        ),
        migrations.AddField(
            model_name='asesorexterno',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodo_del_asesorexterno', to='superusuario.Periodo'),
        ),
    ]
