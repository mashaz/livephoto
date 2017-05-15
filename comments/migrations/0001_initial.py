# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=300, null=True)),
                ('time', models.DateTimeField(null=True)),
            ],
        ),
    ]
