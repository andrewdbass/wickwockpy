from urllib.request import Request, urlopen
import json

req = Request('https://medium.com/_/api/stream/?format=json&to=1476756061722&source=1', headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read().decode('utf-8')
start = data.index('</x>') + 4
data = data[start:]
data = json.loads(data)

arr = []
articlesArray = data['payload']['references']['Post']

for element in articlesArray:
    obj = {};
    obj['title'] = articlesArray[element]['title']
    obj['durration'] = articlesArray[element]['virtuals']['readingTime']
    obj['id'] = articlesArray[element]['id']
    if 'previewImage' in articlesArray[element]['virtuals']:
        obj['image'] = articlesArray[element]['virtuals']['previewImage']["imageId"]
    arr.append(obj)
print(arr)
