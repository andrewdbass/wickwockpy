from apps.articles.models import Article

l = []

articles = Article.objects.all()

for article in articles:
    if articlesArray[article]['title'] not in l:
        l.append(articlesArray[article]['title'])
    else:
        print('duplicate')
