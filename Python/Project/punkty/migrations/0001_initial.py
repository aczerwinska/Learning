# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 07:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herbata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('owner', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='herbata',
            name='punkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punkty.Punkt'),
        ),
    ]
