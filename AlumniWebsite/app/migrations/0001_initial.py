# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('batch', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SCH', 'School'), ('UNV', 'University'), ('BSI', 'Business'), ('HOS', 'Hospital'), ('OTH', 'Others')], max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='alumnus',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Workplace'),
        ),
    ]
