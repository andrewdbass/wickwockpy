from django.core.management.base import BaseCommand
from apps.podcasts.models import Podcast

from urllib.request import Request, urlopen
import json

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def _get_podcasts(self, *args, **kwargs):
        Podcast.objects.all().delete()
        req = Request('http://www.rssmix.com/u/8210270/rss.json', headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read().decode('utf-8')
        data = json.loads(data)
        data = data['channel']['item']
        for podcast in data:
            if podcast['author']:
                if podcast['author']['name']:
                    source = podcast['author']['name']
                else:
                    source = ""
            else:
                source = ""
            if podcast['enclosure']['duration'] is not None:
                duration = int(podcast['enclosure']['duration']/60)
            else:
                durration = 0
            if podcast['enclosure']['link'] is not None:
                link = podcast['enclosure']['link']
            else:
                link = ""
            title = podcast['title']
            description = podcast['description'][:144]
            new = Podcast(source=source, duration=duration, link=link,
            title=title, description=description)
            new.save()
            print(new)

    def handle(self, *args, **options):
        self._get_podcasts()
