from rest_framework import viewsets
from apps.articles.models import Article
from apps.articles.serializers import ArticleSerializer
from apps.tags.models import Tag

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Article.objects.all()
        dur = self.request.query_params.get('duration', None)
        tags = self.request.query_params.getlist('tags', None)

        if tags is not None:
            queryset = queryset.filter(tags__in=tags).distinct()
        if dur is not None:
            queryset = queryset.filter(duration__lte=dur).order_by('-duration','-id')
        return queryset
