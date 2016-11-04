from rest_framework import viewsets
from apps.article_sources.models import ArticleSource
from apps.article_sources.serializers import ArticleSourceSerializer

class ArticleSourceViewSet(viewsets.ModelViewSet):
    queryset = ArticleSource.objects.all()
    serializer_class = ArticleSourceSerializer

    def get_queryset(self):
        queryset = ArticleSource.objects.all()
        return queryset
