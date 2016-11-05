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


    def handle(self, *args, **options):
        l = ""

        articles = Article.objects.all()
        duplicates = 0;
        for article in articles:
            if article.title in l:
                print('duplicate')
                duplicates = duplicates + 1
            else:
                l=l+article.title
                print(len(l))

        print(duplicates)
