# Generated by Django 3.0 on 2019-12-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsesorExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('is_adviserE', 'Is_AdviserE'),),
            },
        ),
        migrations.CreateModel(
            name='AsesorInterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('is_adviserI', 'Is_AdviserI'),),
            },
        ),
    ]
