# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_remove_livephoto_file_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='livephoto',
            name='star',
            field=models.IntegerField(default='0'),
        ),
    ]
