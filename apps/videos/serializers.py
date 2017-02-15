from rest_framework import serializers

from apps.videos.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        depth = 1
