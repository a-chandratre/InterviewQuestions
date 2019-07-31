from lxml import html
import requests

page = requests.get('https://www.marketwatch.com/investing/index/djia?mod=us-markets')
tree = html.fromstring(page.content)

buyers = tree.xpath('//a[@class="link"]/text()')
prices = tree.xpath('//td[@class="table_cell w15 ignore-color"]/text()')

print(buyers)
print(prices)

if 'Apple Inc.' in buyers :
    print("Apple Inc.")
