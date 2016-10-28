from urllib.request import Request, urlopen
import json

req = Request('http://www.rssmix.com/u/8210270/rss.json', headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read().decode('utf-8')
data = json.loads(data)
data = data['channel']['item']
for podcast in data:
    # if podcast['author']:
        # print(podcast['author']['name'])
    # if podcast['enclosure']['duration']:
        # print("empty")
    print("hi")
    if podcast['enclosure']['duration'] is not None:
        print(podcast['enclosure']['duration'])
    # print(podcast['enclosure']['link'])
    # print(podcast['title'])
    # print(podcast['description'])
