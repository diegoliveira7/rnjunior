# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-06 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20170906_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='data_slice_1_scale',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='data_slice_2_scale',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
