# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('article_sources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesource',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
