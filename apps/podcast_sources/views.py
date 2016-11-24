from rest_framework import viewsets
from apps.podcast_sources.models import PodcastSource
from apps.podcast_sources.serializers import PodcastSourceSerializer

class PodcastSourceViewSet(viewsets.ModelViewSet):
    queryset = PodcastSource.objects.all()
    serializer_class = PodcastSourceSerializer

    def get_queryset(self):
        queryset = PodcastSource.objects.all()
        return queryset
