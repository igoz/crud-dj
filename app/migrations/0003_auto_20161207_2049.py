# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 17:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161207_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tv_program',
            old_name='options',
            new_name='commercials',
        ),
        migrations.AlterField(
            model_name='tv_program',
            name='date_prog',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tv_program',
            name='description',
            field=models.CharField(default='description', max_length=300),
        ),
        migrations.AlterField(
            model_name='tv_program',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='tv_program',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]
