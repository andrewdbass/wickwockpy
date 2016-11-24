from __future__ import unicode_literals
from django.db import models

class PodcastSourceType(models.Model):
    podcast_source_type = models.CharField(max_length=144)
    def __str__(self):
        return self.podcast_source_type
