import feedparser
from datetime import datetime
# tags = ['finance', 'investing','personal-finance', 'money', 'fintech','stock-market','economics','banking']
# tags = ['business','entrepreneurship', 'startup', 'marketing', 'small-business', 'business-strategy', 'leadership', 'innovation']
tags = ['business']
count = 0
titles = []
for tag in tags:
    d = feedparser.parse('https://medium.com/feed/tag/'+tag)
    print(datetime(int(d["items"][0]['published'])))
    # items = d['items']
    # for item in items:
    #     if item["title_detail"]['value'] not in titles:
    #         print(item["title_detail"]['value'])
    #         print(item["published"])
    #         titles.append(item["title_detail"]['value'])
    #         count=count+1
print(count)
