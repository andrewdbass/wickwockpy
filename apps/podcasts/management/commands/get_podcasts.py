from django.core.management.base import BaseCommand
from apps.podcasts.models import Podcast
from apps.podcast_sources.models import PodcastSource
from apps.podcast_source_types.models import PodcastSourceType

from urllib.request import Request, urlopen
from time import mktime
import json
import feedparser
from datetime import datetime, timedelta

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def clear_html_tags(self, s):
        if(s.find("<") == -1):
            return s
        elif len(s)<2000:
            print(len(s))
            return self.clear_html_tags(s[:s.find("<")] + s[s.find(">")+1:])
        else:
            return s



    def get_podcasts(self, *args, **kwargs):
        sources = PodcastSource.objects.all()
        podcasts = Podcast.objects.all()
        for source in sources:
            d = feedparser.parse(source.link)
            for item in d['items']:
                if not podcasts.filter(title=item['title']).exists():
                    obj = {}
                    dur1 = 0;
                    dur2 = 0;
                    print(item)
                    obj["title"] = item['title']
                    obj["description"] = self.clear_html_tags(item['summary'])
                    obj["image"] = ""
                    if "image" in item:
                        obj["image"] = item['image']['href']
                    obj["source"] = d['channel']['title']


                    if "links" in item:
                        for link in item['links']:
                            if link['type'] == "audio/mpeg":
                                obj['link'] = link['href']
                                dur1 = int(link['length'])
                            if "itunes_duration" in link:
                                dur2 = link["itunes_duration"]
                    if "itunes_duration" in item:
                        s=item["itunes_duration"]
                        if ":" in s:
                            if (len(s[:s.find(":")])) != 3:
                                hours = int(s[:s.find(":")])
                                s = (s[s.find(":")+1:])
                                minutes = int(s[:s.find(":")])
                                dur2 = hours*60 + minutes
                            else:
                                dur2 = int(s[s.find(":"):])
                        else:
                            dur2 = int(s)/60

                    if dur2 != 0:
                        obj["duration"] = dur2
                    elif dur1 !=0:
                        obj["duration"] = dur1

                    obj["published"] = datetime.fromtimestamp(mktime(item["published_parsed"]))

                    if obj["published"]>=datetime.now()-timedelta(days=5):
                        new_podcast = Podcast.objects.create(
                            title=obj['title'],
                            link=obj['link'],
                            image=obj['image'],
                            source=obj['source'],
                            duration=obj['duration'],
                            published= obj['published']
                            )
                        for tag in source.tags.all():
                            new_podcast.tags.add(tag)
                        print(new_podcast.title)

    def handle(self, *args, **options):
        self.get_podcasts()
