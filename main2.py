import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
res = []
dict = {}

for k1 in root[0]:
    if k1.tag == 'item':
        for k2 in k1:
            dict[k2.tag] = k2.text
        res.append(dict)
        dict = {}
with open('news2.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
