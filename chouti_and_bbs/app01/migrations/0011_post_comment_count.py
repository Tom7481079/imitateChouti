# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20170216_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
