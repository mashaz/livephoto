# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='', max_length=10),
        ),
    ]
