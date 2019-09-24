# Generated by Django 2.0.5 on 2019-09-23 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('nombre_usuario', models.CharField(max_length=50, null=True, unique=True)),
                ('nombres', models.CharField(max_length=100, null=True)),
                ('apellido_paterno', models.CharField(max_length=100, null=True)),
                ('apellido_materno', models.CharField(max_length=100, null=True)),
                ('fecha_nacimiento', models.DateTimeField(null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=11, null=True)),
                ('genero', models.CharField(max_length=65, null=True)),
                ('foto_perfil', models.ImageField(default='default.jpeg', null=True, upload_to='profiles')),
                ('agregado', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
