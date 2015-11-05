# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oficinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_departamento', models.PositiveIntegerField()),
                ('Nombre', models.CharField(max_length=300)),
                ('descripcion', models.TextField(max_length=500)),
            ],
        ),
    ]
