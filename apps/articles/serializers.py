from rest_framework import serializers

from apps.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        depth = 1
