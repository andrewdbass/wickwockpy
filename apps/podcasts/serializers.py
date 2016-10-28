from rest_framework import serializers

from apps.podcasts.models import Podcast

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
