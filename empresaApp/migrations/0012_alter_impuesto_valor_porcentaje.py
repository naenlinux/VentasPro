# Generated by Django 4.2.3 on 2023-10-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresaApp', '0011_rename_nombrecorto_monedas_simbolo_monedas_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impuesto',
            name='valor_porcentaje',
            field=models.IntegerField(default='18'),
        ),
    ]
