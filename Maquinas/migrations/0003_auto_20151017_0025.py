# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maquinas', '0002_cofre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cofre',
            name='id_machine',
            field=models.ForeignKey(default=1, to='Maquinas.Equipo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cofre',
            name='no_serie',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
