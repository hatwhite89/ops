# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-22 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0007_auto_20190922_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriamedicamento',
            name='sub_categoria',
        ),
        migrations.RemoveField(
            model_name='segundasubcategoriamedicamento',
            name='SubSubCatetoria',
        ),
        migrations.RemoveField(
            model_name='subcategoriamedicamento',
            name='SubSubCatetoria',
        ),
        migrations.AddField(
            model_name='categoriamedicamento',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='segundasubcategoriamedicamento',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='subcategoriamedicamento',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='envaseprimario',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='formafarmaceutica',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='viasdeadministracion',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
    ]
