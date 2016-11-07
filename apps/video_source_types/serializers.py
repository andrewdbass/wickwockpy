from rest_framework import serializers

from apps.video_source_types.models import VideoSourceType

class VideoSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSourceType
