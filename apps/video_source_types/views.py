from rest_framework import viewsets
from apps.video_source_types.models import VideoSourceType
from apps.video_source_types.serializers import VideoSourceTypeSerializer

class VideoSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = VideoSourceType.objects.all()
    serializer_class =  VideoSourceTypeSerializer

    def get_queryset(self):
        queryset = VideoSourceType.objects.all()
        return queryset
