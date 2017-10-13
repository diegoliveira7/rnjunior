# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 19:38
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100, verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': '02 - Áreas',
            },
        ),
        migrations.CreateModel(
            name='Assessores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do assessor')),
                ('foto', models.ImageField(upload_to='assessor/%y/%m/%d', verbose_name='Foto do assessor')),
            ],
            options={
                'verbose_name': 'Assessor',
                'verbose_name_plural': '07 - Assessores',
            },
        ),
        migrations.CreateModel(
            name='ClienteNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': '08 - Newsletter',
            },
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do diretor')),
                ('cargo', models.CharField(max_length=150, verbose_name='Cargo')),
                ('foto', models.ImageField(upload_to='diretor/%y/%m/%d', verbose_name='Foto do diretor')),
            ],
            options={
                'verbose_name': 'Diretor',
                'verbose_name_plural': '06 - Diretores',
            },
        ),
        migrations.CreateModel(
            name='EmpresaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100, verbose_name='Nome da empresa')),
                ('foto_empresa', models.ImageField(upload_to='empresa/%y/%m/%d', verbose_name='Foto da empresa')),
                ('email_empresa', models.EmailField(max_length=254, verbose_name='E-mail da empresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': '04 - Empresas',
            },
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('texto', models.CharField(max_length=100, verbose_name='Texto')),
                ('texto_teste', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(help_text='Link da notícia. Não usar caracteres com acentos ou caracteres especiais.', max_length=100, unique=True, verbose_name='Link')),
                ('imagem', models.ImageField(upload_to='noticias/%y/%m/%d', verbose_name='Imagem')),
                ('modificado', models.BooleanField(default=False)),
                ('data_orientation', models.CharField(blank=True, max_length=100)),
                ('data_slice_1', models.SmallIntegerField(blank=True, null=True)),
                ('data_slice_2', models.SmallIntegerField(blank=True, null=True)),
                ('data_slice_1_scale', models.FloatField(blank=True, null=True)),
                ('data_slice_2_scale', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': '01 - Notícias',
            },
        ),
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='parceiros/%y/%m/%d', verbose_name='Imagem')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('texto', models.TextField(verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': '05 - Parceiros',
            },
        ),
        migrations.CreateModel(
            name='SetorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=100, verbose_name='Setor')),
                ('area_referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.AreaModel')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': '03 - Setores',
            },
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='setor_referencia',
            field=models.ManyToManyField(to='home.SetorModel'),
        ),
        migrations.AddField(
            model_name='assessores',
            name='diretor_referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Diretor'),
        ),
    ]
