#!/usr/bin/python
from django.conf import settings
from django.core.management.base import BaseCommand

from apiclient.discovery import build
from apps.videos.models import Video
from apps.video_sources.models import VideoSource
from apps.video_source_types.models import VideoSourceType
import isodate

from datetime import datetime, timedelta

# from apiclient.errors import HttpError
# from oauth2client.tools import argparser


class Command(BaseCommand):

    def read_playlist(self, playlist, pageToken, vids, tags):
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
         items = []
         for item in search['items']:
             print(item)
             item['tags'] = tags
             items.append(item)
         vids.extend(items)

         if 'nextPageToken' in search_response:
           return self.read_playlist(playlist, search_response['nextPageToken'], vids, tags)
         else:
           return vids;
    def read_channel(self, channelName, vids, tags):
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
         if (len(channel['items'])>0):
             playlist = channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
             return self.read_playlist(playlist, None, vids, tags)
         else:
             return vids


    def _get_videos(self):
        sources = VideoSource.objects.all()
        vids = []
        for source in sources:
            if source.video_source_type==VideoSourceType.objects.get(video_source_type="youtube_playlist"):
                vids = self.read_playlist(source.link, None, vids, source.tags)
            if source.video_source_type==VideoSourceType.objects.get(video_source_type="youtube_channel"):
                vids = self.read_channel(source.link, vids, source.tags)
        print(len(vids))

        # Video.objects.all().delete()
        all_videos = Video.objects.all()
        for vid in vids:
            title = vid['snippet']['title']
            link = "https://www.youtube.com/embed/"+vid['id']+"/?autoplay=1&fs=1"
            if 'standard' in vid['snippet']['thumbnails']:
                image = vid['snippet']['thumbnails']['standard']['url']
            else:
                image = vid['snippet']['thumbnails']['default']['url']
            source = "Youtube"
            duration = isodate.parse_duration(vid['contentDetails']['duration']).total_seconds()/60 +1
            tags = vid['tags']
            published = vid['snippet']['publishedAt']
            published = published[:published.find("T")]
            # 2016-11-22T00:29:37.000Z
            date_object = datetime.strptime(published, '%Y-%m-%d')
            print(date_object)
            print(title + " " + link + " " + image + " " + source + " " + str(duration))
            if not all_videos.filter(title=title).exists() and date_object>=datetime.now()-timedelta(days=14):
                new_vid = Video.objects.create(
                title=title,
                link=link,
                image=image,
                source=source,
                duration=int(duration),
                published= date_object
                )
                for tag in tags.all():
                    new_vid.tags.add(tag)
            else:
                print("duplicate or old")



    def handle(self, *args, **options):
        self._get_videos()
