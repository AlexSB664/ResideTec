# Generated by Django 2.2 on 2019-10-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_auto_20191017_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='terminado',
            field=models.BooleanField(default=False),
        ),
    ]