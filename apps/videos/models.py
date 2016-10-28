from __future__ import unicode_literals
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=144)
    link = models.CharField(max_length=144)
    image = models.CharField(max_length=144)
    source = models.CharField(max_length=144)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
