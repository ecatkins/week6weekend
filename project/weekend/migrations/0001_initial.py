# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_time', models.DateTimeField()),
                ('thumbnail_url', models.CharField(max_length=300)),
                ('standard_url', models.CharField(max_length=300)),
                ('likes', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
                ('post_type', models.CharField(max_length=20)),
                ('caption', models.TextField()),
            ],
        ),
    ]
