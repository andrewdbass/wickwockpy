# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastSourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_source_type', models.CharField(max_length=144)),
            ],
        ),
    ]
