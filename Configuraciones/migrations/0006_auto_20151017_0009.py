# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0005_moneda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneda',
            old_name='Abreviacion',
            new_name='CurrencyCode',
        ),
    ]
