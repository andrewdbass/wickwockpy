# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_auto_20161027_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
