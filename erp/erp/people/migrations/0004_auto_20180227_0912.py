# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-27 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180209_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='storage_zone_operable',
            field=models.ManyToManyField(blank=True, related_name='external', to='codenerix_storages.StorageZone', verbose_name='Storage Zone Operable'),
        ),
    ]
