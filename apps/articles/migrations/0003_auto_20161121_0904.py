# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=300),
        ),
    ]
