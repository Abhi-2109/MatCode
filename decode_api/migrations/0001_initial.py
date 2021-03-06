# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-25 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('languages', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('question', models.TextField()),
                ('level', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], max_length=1)),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('input_format', models.TextField()),
                ('output_format', models.TextField()),
                ('constraints', models.TextField()),
                ('marks', models.IntegerField()),
                ('hint', models.TextField(blank=True, null=True)),
                ('solution_cpp', models.TextField(blank=True, null=True)),
                ('solution_python', models.TextField(blank=True, null=True)),
                ('solution_c', models.TextField(blank=True, null=True)),
                ('solution_java', models.TextField(blank=True, null=True)),
                ('input1', models.TextField(blank=True, null=True)),
                ('output1', models.TextField(blank=True, null=True)),
                ('input2', models.TextField(blank=True, null=True)),
                ('output2', models.TextField(blank=True, null=True)),
                ('input3', models.TextField(blank=True, null=True)),
                ('output3', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
