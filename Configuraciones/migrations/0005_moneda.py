# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0004_auto_20151014_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_currency', models.PositiveIntegerField()),
                ('Moneda', models.CharField(max_length=100)),
                ('Abreviacion', models.CharField(max_length=10)),
                ('Denominacion', models.PositiveIntegerField()),
            ],
        ),
    ]
