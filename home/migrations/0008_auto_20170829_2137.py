# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170829_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inteiro',
            name='num',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
