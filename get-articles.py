from urllib.request import Request, urlopen
import json


# Gets about 180 through the first page of tags
# arr = []
# def get_data(req):
#     req = Request(req, headers={'User-Agent': 'Mozilla/5.0'})
#     data = urlopen(req).read().decode('utf-8')
#     start = data.index('</x>') + 4
#     data = data[start:]
#     data = json.loads(data)
#
#     articlesArray = data['payload']['value']
#     for element in articlesArray:
#         if element['title'] not in arr:
#             arr.append(element['title'])
#
# tags = ["business", "startups", "sports", "politics", "technology",
#         "humor", "entertainment", 'life', 'travel', 'user-experience',
#         'design', 'inspiration', 'inovation', 'science', 'history',
#         'adventure','creativity', 'self-improvement', 'photography',
#         'writing', 'ideas','life-lessons']
#
# for tag in tags:
#     get_data("https://medium.com/_/api/tags/"+tag+"/posts?format=json")
#
# print(len(arr))
import urllib.parse

def get_stuff(root, params, l):
    # p = urllib.parse.urlencode(params)
    url = root+"?"+params
    print(url)

    req = Request(url,headers={'User-Agent': 'Opera/9.80'})
    data= urllib.request.urlopen(req).read().decode('utf-8')
    start = data.index('</x>') + 4
    data = data[start:]
    data = json.loads(data)
    if 'Post' not in data['payload']['references']:
        return l
    articlesArray = data['payload']['references']['Post']

    for article in articlesArray:
        # print(article)
        l.append(articlesArray[article]['title'])

    if "paging" in data["payload"]:
        paramString = ""
        # paramString = paramString + "to="+data['payload']["paging"]["next"]["to"]
        paramString = paramString + "page="+ str(data['payload']["paging"]["next"]["page"])
        # for i in data['payload']["paging"]["next"]["ignoredIds"]:
        #     print("hi")
        #     paramString = paramString + "ignoredIds=" + i

        if "api" in root:
            return get_stuff(root, paramString, l)
        return get_stuff("https://www.medium.com"+ data["payload"]["paging"]["path"], paramString, l)
    return(l)

# l = get_stuff("https://medium.com/swlh","format=json",[])
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
l = []
for pub in arr:
    l = get_stuff(pub, "format=json", l)

print(len(l))
# params = urllib.parse.urlencode(
#     {
#         "format": "json",
#
#         "to": "1478194993142",
#         "ignoredIds": [
#           "e4a56c14e47e",
#           "b72999a03d4e",
#           "953e472b5b25",
#           "5e8103392a67",
#           "25f830c16e5",
#           "a7e5a4be3c88",
#           "384902857ec0",
#           "39de3f5e9ae6",
#           "4f0a5081d9e9",
#           "28f95074ce21",
#           "6b1cda5547f0"
#         ],
#         "page": 2
#
#     }
# )
# print("https://medium.com/_/api/collections/b230ea2a6eb8/stream/%s" % params)
# req = Request("https://medium.com/_/api/collections/b230ea2a6eb8/stream?%s" % params, headers={'User-Agent': 'Mozilla/5.0'})
# f = urllib.request.urlopen(req)
# print(f.read())
