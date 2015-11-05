# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(default=1, to='Configuraciones.Pais'),
            preserve_default=False,
        ),
    ]
