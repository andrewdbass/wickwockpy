from rest_framework import viewsets
from apps.videos.models import Video
from apps.videos.serializers import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Video.objects.all()
        dur = self.request.query_params.get('`duration`', None)
        tags = self.request.query_params.getlist('tags', None)

        if tags is not None:
            queryset = queryset.filter(tags__in=tags).distinct()
        if dur is not None:
            queryset = queryset.filter(duration__lte=dur).order_by('-duration','-id')
        return queryset
