# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-25 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20160812_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='playlist',
            field=models.BooleanField(default=False),
        ),
    ]
