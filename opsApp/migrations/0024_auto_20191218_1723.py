# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0023_auto_20191218_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formafarmaceutica',
            name='nombre_forma',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='viasdeadministracion',
            name='nombre_via_administracion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]