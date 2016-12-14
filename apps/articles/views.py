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
        article_id = self.request.query_params.get('id', None)
        print(dur)
        if len(tags) != 0 and dur is not None:
            queryset = queryset.filter(tags__in=tags).distinct()
            queryset = queryset.filter(duration__lte=dur).order_by('-duration','-id')
        if article_id is not None:
            queryset = queryset.filter(id=article_id)
        # else:
        #     queryset= None;
        return queryset

class ArticleDetailViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        article_id = self.request.query_params.get('id', None)
        queryset = Article.objects.get(article_id)

        return queryset
