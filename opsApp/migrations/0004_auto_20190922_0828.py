# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-22 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opsApp', '0003_auto_20190921_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaFarmaceutica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_forma', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ViasDeAdministracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_via_administracion', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='forma_farmaceutica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opsApp.FormaFarmaceutica'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='sub_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opsApp.SubCategoriaMedicamento'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='via_de_administracion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opsApp.ViasDeAdministracion'),
        ),
    ]
