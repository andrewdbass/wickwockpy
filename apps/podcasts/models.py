from __future__ import unicode_literals
from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    source = models.CharField(max_length=500)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
