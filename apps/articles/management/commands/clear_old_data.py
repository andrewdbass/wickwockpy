from django.core.management.base import BaseCommand
from apps.articles.models import Article
from apps.videos.models import Video
from apps.podcasts.models import Podcast

from datetime import datetime, timedelta

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def handle(self, *args, **options):
        Article.objects.all().filter(published__lte=datetime.now()-timedelta(days=1)).delete()
        # Video.objects.all().filter(published__lte=datetime.now()-timedelta(days=1)).delete()
        # Postcast.objects.all().filter(published__lte=datetime.now()-timedelta(days=1)).delete()
