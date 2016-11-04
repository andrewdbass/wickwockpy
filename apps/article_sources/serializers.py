from rest_framework import serializers

from apps.article_sources.models import ArticleSource

class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
