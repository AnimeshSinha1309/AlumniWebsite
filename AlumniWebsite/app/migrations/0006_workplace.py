# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160423_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SCH', 'School'), ('UNV', 'University'), ('BSI', 'Business'), ('HOS', 'Hospital'), ('OTH', 'Others')], max_length=3)),
            ],
        ),
    ]
