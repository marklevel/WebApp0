# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0004_auto_20151014_0300'),
        ('Maquinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cofre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cofre', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=300)),
                ('ubicacion', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=500)),
                ('ciudad', models.ForeignKey(to='Configuraciones.Ciudade')),
                ('estado', models.ForeignKey(to='Configuraciones.Estado')),
                ('pais', models.ForeignKey(to='Configuraciones.Pai')),
            ],
        ),
    ]
