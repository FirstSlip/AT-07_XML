import itertools
import json
from urllib.request import urlopen
from json import loads


def grouper(item):
    return item['timestamp'][0:10]


revisions = []
res = {}
counter = 0
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
for i in data['query']['pages']['183903']['revisions']:
    revisions.append(i)
for key, group_items in itertools.groupby(revisions, key=grouper):
    for item in group_items:
        counter += 1
    res[key] = counter
    counter = 0
with open('wiki.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
