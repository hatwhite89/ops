# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-22 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0008_auto_20190922_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='antibiotico_reserva',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='establecimiento',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='lista_complementaria',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='restriccion_uso',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
