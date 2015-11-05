# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_sucursal', models.PositiveIntegerField()),
                ('Nombre', models.CharField(max_length=300)),
                ('ubicacion', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
    ]
