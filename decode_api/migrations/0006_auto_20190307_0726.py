# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_api', '0005_templatecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatecode',
            name='compiler',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='templatecode',
            name='memory_limit',
            field=models.CharField(default='150Mb', max_length=20),
        ),
        migrations.AddField(
            model_name='templatecode',
            name='time_limit',
            field=models.CharField(default='10 Sec', max_length=18),
        ),
    ]
