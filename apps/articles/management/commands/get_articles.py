from django.core.management.base import BaseCommand
from apps.articles.models import Article

from urllib.request import Request, urlopen
import json

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def readData(self, to):
        if to == "":
            req = Request('https://medium.com/_/api/stream/?format=json', headers={'User-Agent': 'Mozilla/5.0'})
        else:
            req = Request('https://medium.com/_/api/stream/?format=json&to='+ str(to)    +'&source=1', headers={'User-Agent': 'Mozilla/5.0'})

        data = urlopen(req).read().decode('utf-8')
        start = data.index('</x>') + 4
        data = data[start:]
        data = json.loads(data)
        arr = []
        articlesArray = data['payload']['references']['Post']

        for element in articlesArray:
            obj = {};
            obj['title'] = articlesArray[element]['title']
            obj['duration'] = articlesArray[element]['virtuals']['readingTime']
            obj['link'] = 'https://www.medium.com/posts/' + articlesArray[element]['id']
            if 'previewImage' in articlesArray[element]['virtuals']:
                obj['image'] = articlesArray[element]['virtuals']['previewImage']["imageId"]
            arr.append(obj)
            new = Article(title = obj['title'], link = obj['link'], duration = obj['duration'], image = obj['image'], source = 'Medium')
            new.save()
        print(arr)

        return data["payload"]['paging']['next']['to']

    def _get_articles(self, *args, **kwargs):
        Article.objects.all().delete()
        to = ""
        for i in range(20):
            to = self.readData(to)

    def handle(self, *args, **options):
        self._get_articles()
