# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-05 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='street',
            field=models.CharField(blank=True, max_length=500, verbose_name='Street'),
        ),
    ]