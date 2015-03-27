#! /usr/bin/python3
# -*- coding: utf-8 -*-

import csv
from lxml import html

def parse_item(item):
    return {
        'speaker': item.xpath('.//h4[@class="h12 talk-link__speaker"]/text()')[0],
        'title': item.xpath('.//h4[@class="h9 m5"]/a/text()')[0].strip('\n'),
        'href': item.xpath('.//h4[@class="h9 m5"]/a/@href')[0],
        'views': item.xpath('.//span[@class="meta__val"]/text()')[0].split('\n')[1],
        'date': item.xpath('.//span[@class="meta__val"]/text()')[1].strip('\n')
    }


npages = 3

print('Parse pages.')
data = []
for page_num in range(1, npages+1):
    print(page_num)
    root = html.parse('http://www.ted.com/talks?page=%s' % page_num)
    items = root.xpath('//div[@id="browse-results"]//div[@class="col"]')
    for item in items:
        d = parse_item(item)
        data.append(d)

print('Save data to file.')
with open('data.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print('Done.')
