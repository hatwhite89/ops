# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-20 01:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0028_viasdeadministracion_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='nombre_medicamento',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
