from rest_framework import viewsets
from apps.video_sources.models import VideoSource
from apps.video_sources.serializers import VideoSourceSerializer

class VideoSourceViewSet(viewsets.ModelViewSet):
    queryset = VideoSource.objects.all()
    serializer_class = VideoSourceSerializer

    def get_queryset(self):
        queryset = VideoSource.objects.all()
        return queryset
