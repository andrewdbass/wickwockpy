# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]