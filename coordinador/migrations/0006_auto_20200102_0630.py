# Generated by Django 2.2 on 2020-01-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superusuario', '0001_initial'),
        ('coordinador', '0005_oferta_carrera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='carrera',
        ),
        migrations.AddField(
            model_name='oferta',
            name='carrera',
            field=models.ManyToManyField(to='superusuario.Carrera'),
        ),
    ]
