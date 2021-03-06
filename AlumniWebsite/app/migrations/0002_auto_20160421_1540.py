# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('FR', 'Friends'), ('AQ', 'Acquaintences')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='alumnus',
            name='email',
        ),
        migrations.AddField(
            model_name='circle',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_friend', to='app.Alumnus'),
        ),
        migrations.AddField(
            model_name='circle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_user', to='app.Alumnus'),
        ),
    ]
