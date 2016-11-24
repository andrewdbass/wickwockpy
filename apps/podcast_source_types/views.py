from rest_framework import viewsets
from apps.podcast_source_types.models import PodcastSourceType
from apps.podcast_source_types.serializers import PodcastSourceTypeSerializer

class PodcastSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = PodcastSourceType.objects.all()
    serializer_class = PodcastSourceTypeSerializer

    def get_queryset(self):
        queryset = PodcastSourceType.objects.all()
        return queryset
