# Generated by Django 4.2.3 on 2023-08-19 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0009_almacenprecioum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almacen',
            name='precioDocena',
        ),
        migrations.RemoveField(
            model_name='almacen',
            name='precioPaquete',
        ),
        migrations.RemoveField(
            model_name='almacen',
            name='precioUnidad',
        ),
    ]
