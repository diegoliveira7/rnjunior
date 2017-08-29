# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 02:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_noticias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticias',
            options={'verbose_name': 'Notícia'},
        ),
        migrations.AddField(
            model_name='noticias',
            name='imagem',
            field=models.ImageField(default=datetime.datetime(2017, 8, 29, 2, 3, 45, 170216, tzinfo=utc), upload_to='media/%y/%m/%d', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
