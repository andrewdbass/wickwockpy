import feedparser
from datetime import datetime, timedelta
import time

# print(datetime.strptime("Wed, 23 Nov 2016 14:40:18 GMT", "%a, %d %b %Y %H:%M:%S %Z"))

# tags = ['finance', 'investing','personal-finance', 'money', 'fintech','stock-market','economics','banking']
# tags = ['business','entrepreneurship', 'startup', 'marketing', 'small-business', 'business-strategy', 'leadership', 'innovation']
def clear_html_tags(s):
    if(s.find("<") == -1):
        return s
    else:
        return clear_html_tags(s[:s.find("<")] + s[s.find(">")+1:])

# d = feedparser.parse("http://feeds.feedburner.com/thetimferrissshow?format=xml")
d = feedparser.parse("http://simplecast.com/podcasts/1376/rss")
# d = feedparser.parse("http://www.npr.org/rss/podcast.php?id=510289")
# t = datetime.strptime(d["items"][0]['published'], "%a, %d %b %Y %H:%M:%S %Z")
# print(t>=datetime.now()-timedelta(days=1))
# print("hi")

for item in d['items']:
    dur1 = 0;
    dur2 = 0;
    print(item)
    print(item['title'])
    print(clear_html_tags(item['summary']))
    if "image" in item:
        print(item['image']['href'])
    print(d['channel']['title'])


    if "links" in item:
        for link in item['links']:
            if link['type'] == "audio/mpeg":
                print(link['href'])
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
        print(dur2)
    elif dur1 !=0:
        print(dur1)
    else:
        print("failed")

    print("TAGS")
