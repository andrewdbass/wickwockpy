from rest_framework import viewsets
from apps.article_source_types.models import ArticleSourceType
from apps.article_source_types.serializers import ArticleSourceTypeSerializer

class ArticleSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = ArticleSourceType.objects.all()
    serializer_class = ArticleSourceTypeSerializer

    def get_queryset(self):
        queryset = ArticleSourceType.objects.all()
        return queryset
