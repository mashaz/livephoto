# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='upload_sum',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='1', max_length=10),
        ),
    ]