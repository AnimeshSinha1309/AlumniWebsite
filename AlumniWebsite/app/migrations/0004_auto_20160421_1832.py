# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160421_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnus',
            name='picture',
            field=models.ImageField(default='profile/_defaultavatar.png', upload_to='profile/'),
        ),
    ]
