# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='用户名'),
        ),
    ]
