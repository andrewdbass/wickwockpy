from __future__ import unicode_literals
from django.db import models

class PodcastSource(models.Model):
    link = models.CharField(max_length=144)
    podcast_source_type = models.ForeignKey("podcast_source_types.PodcastSourceType")
    tags = models.ManyToManyField("tags.Tag")
    def __str__(self):
        return self.link
