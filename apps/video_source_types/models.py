from __future__ import unicode_literals
from django.db import models

class VideoSourceType(models.Model):
    video_source_type = models.CharField(max_length=144)
    def __str__(self):
        return self.video_source_type
