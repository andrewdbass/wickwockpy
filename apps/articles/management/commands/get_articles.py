from django.core.management.base import BaseCommand
from apps.articles.models import Article
from apps.article_sources.models import ArticleSource
from apps.article_source_types.models import ArticleSourceType

from urllib.request import Request, urlopen
import urllib.parse

import json
import random

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def get_articles_from_medium_publications(self, root, params, l):
        # p = urllib.parse.urlencode(params)
        url = root+"?"+params
        print(url)
        if bool(random.getrandbits(1)):
            req = Request(url,headers={'User-Agent': 'Opera/9.80'})
        else:
            req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})

        data= urllib.request.urlopen(req).read().decode('utf-8')
        start = data.index('</x>') + 4
        data = data[start:]
        data = json.loads(data)
        if 'Post' not in data['payload']['references']:
            return l
        articlesArray = data['payload']['references']['Post']

        for article in articlesArray:
            print(article)
            if articlesArray[article]['title'] not in l:
                obj = {};
                obj['title'] = articlesArray[article]['title']
                obj['duration'] = articlesArray[article]['virtuals']['readingTime']+1
                obj['link'] = 'https://www.medium.com/posts/' + articlesArray[article]['id']
                if 'previewImage' in articlesArray[article]['virtuals']:
                    obj['image'] = articlesArray[article]['virtuals']['previewImage']["imageId"]
                new = Article(title = obj['title'], link = obj['link'], duration = obj['duration'], image = obj['image'], source = 'Medium')
                new.save()
                l.append(obj['title'])

        if "paging" in data["payload"]:
            paramString = ""
            # paramString = paramString + "to="+data['payload']["paging"]["next"]["to"]
            paramString = paramString + "page="+ str(data['payload']["paging"]["next"]["page"])
            # for i in data['payload']["paging"]["next"]["ignoredIds"]:
            #     print("hi")
            #     paramString = paramString + "ignoredIds=" + i

            if "api" in root:
                return self.get_articles_from_medium_publications(root, paramString, l)
            return self.get_articles_from_medium_publications("https://www.medium.com"+ data["payload"]["paging"]["path"], paramString, l)
        return(l)

    # def readData(self, to):
    #     if to == "":
    #         req = Request('https://medium.com/_/api/stream/?format=json', headers={'User-Agent': 'Mozilla/5.0'})
    #     else:
    #         req = Request('https://medium.com/_/api/stream/?format=json&to='+ str(to)    +'&source=1', headers={'User-Agent': 'Mozilla/5.0'})
    #
    #     data = urlopen(req).read().decode('utf-8')
    #     start = data.index('</x>') + 4
    #     data = data[start:]
    #     data = json.loads(data)
    #     arr = []
    #     articlesArray = data['payload']['references']['Post']
    #
    #     for element in articlesArray:
    #         obj = {};
    #         obj['title'] = articlesArray[element]['title']
    #         obj['duration'] = articlesArray[element]['virtuals']['readingTime']
    #         obj['link'] = 'https://www.medium.com/posts/' + articlesArray[element]['id']
    #         if 'previewImage' in articlesArray[element]['virtuals']:
    #             obj['image'] = articlesArray[element]['virtuals']['previewImage']["imageId"]
    #         arr.append(obj)
    #         new = Article(title = obj['title'], link = obj['link'], duration = obj['duration'], image = obj['image'], source = 'Medium')
    #         new.save()
    #     print(arr)
    #
    #     return data["payload"]['paging']['next']['to']
    #
    # def _get_articles(self, *args, **kwargs):
    #     Article.objects.all().delete()
    #     to = ""
    #     for i in range(20):
    #         to = self.readData(to)

    # def get_data(self, req, arr):
    #     req = Request(req, headers={'User-Agent': 'Mozilla/5.0'})
    #     data = urlopen(req).read().decode('utf-8')
    #     start = data.index('</x>') + 4
    #     data = data[start:]
    #     data = json.loads(data)
    #
    #     articlesArray = data['payload']['value']
    #     for element in articlesArray:
    #         if element['title'] not in arr:
    #             print("hi")
    #             obj = {};
    #             obj['title'] = element['title']
    #             obj['duration'] = element['virtuals']['readingTime']
    #             obj['link'] = 'https://www.medium.com/posts/' + element['id']
    #             if 'previewImage' in element['virtuals']:
    #                 obj['image'] = element['virtuals']['previewImage']["imageId"]
    #             new = Article(title = obj['title'], link = obj['link'], duration = obj['duration'], image = obj['image'], source = 'Medium')
    #             new.save()
    #             arr.append(obj['title'])
    #
    #     return arr

    def handle(self, *args, **options):
        l = []
        Article.objects.all().delete();
        a = ArticleSource.objects.all()
        medium = ArticleSourceType.objects.get(article_source_type="medium_publication")
        print(medium)

        for source in a:
         if source.article_source_type == medium :
             self.get_articles_from_medium_publications(source.link,"format=json",l)

        print(len(l))
        # Article.objects.all().delete()
        # # self._get_articles()
        # arr = []
        #
        # tags = ["business", "startups", "sports", "politics", "technology",
        #         "humor", "entertainment", 'life', 'travel', 'user-experience',
        #         'design', 'inspiration', 'inovation', 'science', 'history',
        #         'adventure','creativity', 'self-improvement', 'photography',
        #         'writing', 'ideas','life-lessons']
        #
        # for tag in tags:
        #     arr.append(self.get_data("https://medium.com/_/api/tags/"+tag+"/posts?format=json", arr))
        # self.get_data()
