from __future__ import unicode_literals
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return self.name
