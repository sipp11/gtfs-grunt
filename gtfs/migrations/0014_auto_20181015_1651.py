# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0013_auto_20181015_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farerule',
            name='contains_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Contains ID'),
        ),
        migrations.AlterField(
            model_name='farerule',
            name='destination_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Destination ID'),
        ),
    ]
