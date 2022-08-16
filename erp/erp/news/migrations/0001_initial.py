# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-17 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=150, null=True, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('web_from', models.DateTimeField(verbose_name='Mostrar en la página web de')),
                ('web_until', models.DateTimeField(blank=True, null=True, verbose_name='Mostrar en la página web hasta')),
                ('main_from', models.DateTimeField(verbose_name='Mostrar en la página principal de')),
                ('main_until', models.DateTimeField(verbose_name='Mostrar en la página principal hasta')),
                ('public', models.BooleanField(default=False, verbose_name='Público')),
                ('language', models.CharField(choices=[('es', 'Spanish'), ('en', 'English')], max_length=10, verbose_name='Lenguaje')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
    ]