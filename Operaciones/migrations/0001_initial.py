# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maquinas', '0002_cofre'),
        ('Oficinas', '0002_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colecta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_transaccion', models.PositiveIntegerField()),
                ('cajero', models.PositiveIntegerField()),
                ('unidades', models.PositiveIntegerField()),
                ('denominacion', models.PositiveIntegerField()),
                ('id_cofre', models.ForeignKey(to='Maquinas.Cofre')),
                ('id_departamento', models.ForeignKey(to='Oficinas.Departamento')),
                ('id_sucursal', models.ForeignKey(to='Oficinas.Sucursale')),
            ],
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_transaccion', models.PositiveIntegerField()),
                ('cajero', models.PositiveIntegerField()),
                ('unidades', models.PositiveIntegerField()),
                ('denominacion', models.PositiveIntegerField()),
                ('id_cofre', models.ForeignKey(to='Maquinas.Cofre')),
                ('id_departamento', models.ForeignKey(to='Oficinas.Departamento')),
                ('id_sucursal', models.ForeignKey(to='Oficinas.Sucursale')),
            ],
        ),
        migrations.CreateModel(
            name='Estatu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_mensaje', models.PositiveIntegerField()),
                ('cajero', models.PositiveIntegerField()),
                ('id_cofre', models.ForeignKey(to='Maquinas.Cofre')),
                ('id_departamento', models.ForeignKey(to='Oficinas.Departamento')),
                ('id_sucursal', models.ForeignKey(to='Oficinas.Sucursale')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_mensaje', models.PositiveIntegerField()),
                ('cajero', models.PositiveIntegerField()),
                ('id_cofre', models.ForeignKey(to='Maquinas.Cofre')),
                ('id_departamento', models.ForeignKey(to='Oficinas.Departamento')),
                ('id_sucursal', models.ForeignKey(to='Oficinas.Sucursale')),
            ],
        ),
    ]
