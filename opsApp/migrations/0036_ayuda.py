# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-20 03:20
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0035_auto_20191219_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ayuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
    ]