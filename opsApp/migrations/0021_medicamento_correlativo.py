# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-25 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0020_categoriamedicamento_correlativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='correlativo',
            field=models.IntegerField(null=True),
        ),
    ]