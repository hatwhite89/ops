# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-24 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0011_archivosgaceta_establecimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='establecimiento2',
            field=models.ManyToManyField(to='opsApp.Establecimiento'),
        ),
    ]
