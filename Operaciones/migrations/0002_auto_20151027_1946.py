# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colecta',
            name='fecha_colec',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='deposito',
            name='fecha_depo',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='estatu',
            name='fecha_esta',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='fecha_event',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
