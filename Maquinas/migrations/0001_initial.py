# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_machine', models.PositiveIntegerField()),
                ('marca', models.CharField(max_length=300)),
                ('modelo', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
    ]
