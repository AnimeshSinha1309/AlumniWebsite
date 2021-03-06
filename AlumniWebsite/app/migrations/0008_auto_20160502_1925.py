# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_workplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnus',
            name='admission_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='current_address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='permanent_address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='phone_home',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='phone_mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='phone_work',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='relationship_status',
            field=models.CharField(choices=[('MR', 'Married'), ('SN', 'Single'), ('RL', 'In a Relationship'), ('DV', 'Divorced, Currently Single')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('L', 'Lesbian'), ('G', 'Gay'), ('B', 'Bisexual'), ('T', 'Transgender'), ('Q', 'Queer')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='validity_code',
            field=models.CharField(choices=[('V', 'Validated'), ('P', 'Paid'), ('U', 'Unchecked'), ('B', 'Blocked')], default='U', max_length=1),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Random Description about some random stuff. No idea what to put here, will get the data soon.', max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='subtitle',
            field=models.CharField(default='Just do your thing.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='batch',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='jobtitle',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='workplace',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
