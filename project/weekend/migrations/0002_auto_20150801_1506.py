# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='event',
            field=models.CharField(default='gay', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instagram',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
    ]
