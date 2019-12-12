# Generated by Django 3.0 on 2019-12-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoControl', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('semetre', models.IntegerField(null=True)),
            ],
            options={
                'permissions': (('is_student', 'Is_Student'),),
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('estatus', models.CharField(max_length=50, null=True)),
                ('terminado', models.BooleanField(default=False)),
            ],
        ),
    ]
