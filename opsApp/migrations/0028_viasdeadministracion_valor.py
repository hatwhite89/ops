# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-19 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0027_remove_viasdeadministracion_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='viasdeadministracion',
            name='valor',
            field=models.BooleanField(default=False),
        ),
    ]
