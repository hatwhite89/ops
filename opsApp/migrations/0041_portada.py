# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-19 20:56
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0040_auto_20200203_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='portada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
