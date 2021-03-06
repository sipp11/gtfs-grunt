# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 17:16
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0003_auto_20180525_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gtfs.Agency'),
        ),
        migrations.AlterField(
            model_name='route',
            name='desc',
            field=models.CharField(blank=True, max_length=250, verbose_name='Route desc'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_color',
            field=models.CharField(blank=True, max_length=6, verbose_name='Route color'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_sort_order',
            field=models.IntegerField(blank=True, default=0, verbose_name='Route sort order'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_text_color',
            field=models.CharField(blank=True, max_length=6, verbose_name='Route text color'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_url',
            field=models.CharField(blank=True, max_length=240, verbose_name='Route URL'),
        ),
        migrations.AlterField(
            model_name='route',
            name='shapes',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326),
        ),
    ]
