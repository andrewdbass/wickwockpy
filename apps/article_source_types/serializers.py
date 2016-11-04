from rest_framework import serializers

from apps.article_source_types.models import ArticleSourceType

class ArticleSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSourceType
