from rest_framework import serializers

from apps.podcast_sources.models import PodcastSource

class PodcastSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastSource
