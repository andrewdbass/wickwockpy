from __future__ import unicode_literals
from django.db import models

class ArticleSource(models.Model):
    link = models.CharField(max_length=144)
    article_source_type = models.ForeignKey("article_source_types.ArticleSourceType")
    tags = models.ManyToManyField("tags.Tag")
    def __str__(self):
        return self.link
