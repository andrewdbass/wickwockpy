from __future__ import unicode_literals
from django.db import models

class VideoSource(models.Model):
    link = models.CharField(max_length=144)
    video_source_type = models.ForeignKey("video_source_types.VideoSourceType")
    def __str__(self):
        return self.link
