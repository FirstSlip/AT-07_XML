import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
res = []
dict = {'pubDate': '', 'title': ''}

for k1 in root[0]:
    if k1.tag == 'item':
        for k2 in k1:
            if k2.tag == 'title':
                dict['title'] = k2.text
            if k2.tag == 'pubDate':
                dict['pubDate'] = k2.text
    if dict['pubDate'] != '' and dict['title'] != '':
        res.append(dict)
        dict = {'pubDate': '', 'title': ''}
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
