from rest_framework import viewsets
from apps.podcasts.models import Podcast
from apps.podcasts.serializers import PodcastSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Podcast.objects.all()
        dur = self.request.query_params.get('duration', None)
        if dur is not None:
            queryset = queryset.filter(duration__lte=dur).order_by('-duration','-id')
        return queryset
