from django.core.management.base import BaseCommand
from apps.articles.models import Article
from apps.article_sources.models import ArticleSource
from apps.article_source_types.models import ArticleSourceType

from urllib.request import Request, urlopen
import json

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def handle(self, *args, **options):
        arr = [
        "https://medium.com/swlh",
        "https://medium.com/matter",
        "https://medium.com/startup-grind",
        "https://medium.com/due",
        "https://medium.com/thewashingtonpost",
        "https://medium.com/the-white-house",
        "https://medium.com/hillary-for-america",
        "https://medium.com/the-coffeelicious",
        "https://medium.com/personal-growth",
        "https://byrslf.co",
        "https://medium.com/marketing-and-entrepreneurship",
        "https://uxdesign.cc/",
        "https://readthink.com/",
        "https://theringer.com/",
        "https://medium.com/bright",
        "https://medium.com/mother-jones",
        "https://travel.hostfully.com/",
        "https://m.signalvnoise.com/",
        "https://medium.com/hi-my-name-is-jon",
        "https://500ish.com/",
        "https://thecauldron.si.com/",
        "https://medium.com/the-players-tribune",
        "https://medium.com/sportspickle",
        "https://medium.com/bill-melinda-gates-foundation",
        "https://medium.com/slackjaw",
        "https://medium.com/the-nib",
        "https://theawl.com",
        "https://hackernoon.com",
        "https://filmschoolrejects.com",
        "https://howwegettonext.com",
        "https://thebillfold.com",
        "https://medium.com/poets-unlimited",
        "https://timeline.com",
        "https://medium.com/art-of-practicality",
        "https://medium.com/cinenation-show",
        "https://theinsider.com",
        "https://sto-glo.com",
        "https://medium.com/cuepoint",
        "https://medium.com/the-cube",
        "https://nexus.vert.gg/",
        "https://thinkprogress.org/",
        "https://medium.com/foggy-bottom",
        "https://medium.com/news-politics",
        "https://medium.com/the-guardian-us",
        "https://hdp.press/",
        "https://medium.com/national-post",
        "https://news.cheddar.com/",
        "https://extranewsfeed.com/",
        "https://fashionbits.in/",
        "https://medium.com/online-shopping-tips",
        "https://medium.com/this-tailored-life",
        "https://medium.com/gone",
        'https://medium.com/cultural-facts',
        "https://medium.com/life-hacking-2",
        ]
        t = ArticleSourceType.objects.filter(id=1)[0]
        for s in arr:
            a = ArticleSource(link=s,article_source_type=t)
            print(a)
            a.save()
