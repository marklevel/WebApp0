# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuraciones', '0003_ciudad'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ciudad',
            new_name='Ciudade',
        ),
        migrations.RenameModel(
            old_name='Pais',
            new_name='Pai',
        ),
    ]
