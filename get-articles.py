from urllib.request import Request, urlopen
import json
arr = []

def get_data(req):
    req = Request(req, headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(req).read().decode('utf-8')
    start = data.index('</x>') + 4
    data = data[start:]
    data = json.loads(data)

    articlesArray = data['payload']['value']
    for element in articlesArray:
        if element['title'] not in arr:
            arr.append(element['title'])

tags = ["business", "startups", "sports", "politics", "technology",
        "humor", "entertainment", 'life', 'travel', 'user-experience',
        'design', 'inspiration', 'inovation', 'science', 'history',
        'adventure','creativity', 'self-improvement', 'photography',
        'writing', 'ideas','life-lessons']

for tag in tags:
    get_data("https://medium.com/_/api/tags/"+tag+"/posts?format=json")

print(len(arr))
