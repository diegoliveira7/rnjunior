# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-12 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20170912_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresamodel',
            name='setor_referencia',
            field=models.ManyToManyField(to='home.SetorModel'),
        ),
    ]
