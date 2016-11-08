#!/usr/bin/python
from django.conf import settings
from django.core.management.base import BaseCommand

from apiclient.discovery import build
from apps.videos.models import Video
from apps.video_sources.models import VideoSource
from apps.video_source_types.models import VideoSourceType
import isodate
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser


class Command(BaseCommand):

    def read_playlist(self, playlist, pageToken, vids):
         DEVELOPER_KEY = settings.GOOGLE_API_KEY
         YOUTUBE_API_SERVICE_NAME = "youtube"
         YOUTUBE_API_VERSION = "v3"
         list_of_video_ids = []

         youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)

         search_response = youtube.playlistItems().list(
           playlistId=playlist,
           part="id,snippet,contentDetails",
           pageToken=pageToken,
           maxResults="50"
         ).execute()
         for item in search_response['items']:
           list_of_video_ids.append(item['snippet']['resourceId']['videoId'])

         list_of_video_ids = ",".join(list_of_video_ids)
         print(list_of_video_ids)
         search = youtube.videos().list(
           id=list_of_video_ids,
           part="id,snippet,contentDetails",
           maxResults="50"
         ).execute()
         vids.extend(search['items'])

         if 'nextPageToken' in search_response:
           return self.read_playlist(playlist, search_response['nextPageToken'], vids)
         else:
           return vids;
    def read_channel(self, channelName, vids):
         DEVELOPER_KEY = settings.GOOGLE_API_KEY
         YOUTUBE_API_SERVICE_NAME = "youtube"
         YOUTUBE_API_VERSION = "v3"
         list_of_video_ids = []

         youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)

         channel = youtube.channels().list(
             part="id,contentDetails",
             forUsername=channelName
         ).execute()

         playlist = channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
         return self.read_playlist(playlist, None, vids)


    def _get_videos(self):
        sources = VideoSource.objects.all()
        vids = []
        for source in sources:
            if source.video_source_type==VideoSourceType.objects.get(video_source_type="youtube_playlist"):
                vids = self.read_playlist(source.link, None, vids)
            if source.video_source_type==VideoSourceType.objects.get(video_source_type="youtube_channel"):
                vids = self.read_channel(source.link, vids)
        print(len(vids))

        Video.objects.all().delete()
        for vid in vids:

            title = vid['snippet']['title']
            link = "https://www.youtube.com/embed/"+vid['id']+"/?autoplay=1&fs=1"
            if 'standard' in vid['snippet']['thumbnails']:
                image = vid['snippet']['thumbnails']['standard']['url']
            else:
                image = vid['snippet']['thumbnails']['default']['url']
            source = "Youtube"
            duration = isodate.parse_duration(vid['contentDetails']['duration']).total_seconds()/60 +1
            print(title + " " + link + " " + image + " " + source + " " + str(duration))
            new_vid = Video(title=title, link=link, image=image, source=source, duration=int(duration))
            new_vid.save()


    def handle(self, *args, **options):
        self._get_videos()
