from rest_framework import serializers

from apps.podcast_source_types.models import PodcastSourceType

class PodcastSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastSourceType
