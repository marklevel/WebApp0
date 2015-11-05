# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0002_estado_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idCity', models.PositiveIntegerField()),
                ('city_name', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(to='Configuraciones.Estado')),
            ],
        ),
    ]
