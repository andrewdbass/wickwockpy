from rest_framework import serializers

from apps.video_sources.models import VideoSource

class VideoSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSource
