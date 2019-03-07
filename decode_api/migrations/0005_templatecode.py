# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decode_api', '0004_compile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.CharField(max_length=2)),
                ('template_code', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
