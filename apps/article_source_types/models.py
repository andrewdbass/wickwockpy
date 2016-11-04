from __future__ import unicode_literals
from django.db import models

class ArticleSourceType(models.Model):
    article_source_type = models.CharField(max_length=144)
    def __str__(self):
        return self.article_source_type
