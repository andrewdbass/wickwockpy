#!/usr/bin/python
from django.conf import settings
from django.core.management.base import BaseCommand

from apiclient.discovery import build
from apps.videos.models import Video
import isodate
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser


class Command(BaseCommand):

    def read_playlist(self, pageToken, data):
         DEVELOPER_KEY = settings.GOOGLE_API_KEY
         YOUTUBE_API_SERVICE_NAME = "youtube"
         YOUTUBE_API_VERSION = "v3"
         list_of_video_ids = []

         youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)

         search_response = youtube.playlistItems().list(
           playlistId="PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-",
           part="id,snippet,contentDetails",
           pageToken=pageToken,
           maxResults="50"
         ).execute()
         for item in search_response['items']:
           list_of_video_ids.append(item['snippet']['resourceId']['videoId'])

         list_of_video_ids = ",".join(list_of_video_ids)

         search = youtube.videos().list(
           id=list_of_video_ids,
           part="id,snippet,contentDetails",
           maxResults="50"
         ).execute()
         data.append(search['items'])

         if 'nextPageToken' in search_response:
           return self.read_playlist(search_response['nextPageToken'], data)
         else:
           return data;


    def _get_videos(self):
        vids = self.read_playlist(None,[])
        vids = [val for sublist in vids for val in sublist]
        Video.objects.all().delete()
        for vid in vids:

            title = vid['snippet']['title']
            link = "https://www.youtube.com/embed/"+vid['id']+"/?autoplay=1&fs=1"
            if 'standard' in vid['snippet']['thumbnails']:
                image = vid['snippet']['thumbnails']['standard']['url']
            else:
                image = vid['snippet']['thumbnails']['default']['url']
            source = "Youtube"
            duration = isodate.parse_duration(vid['contentDetails']['duration']).total_seconds()/60
            print(title + " " + link + " " + image + " " + source + " " + str(duration))
            new_vid = Video(title=title, link=link, image=image, source=source, duration=int(duration))
            new_vid.save()


    def handle(self, *args, **options):
        self._get_videos()
