from bs4 import BeautifulSoup

with open('sample_listings.html', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.price'):
    print(tag.text)

selectors = ['.item', '.badge', '.free-shipping', '.sponsored',
             '#results > li', '.item + .item', 'li.item > a']
# Predictions:
# .item           -> 8
# .badge          -> 5
# .free-shipping  -> 3
# .sponsored      -> 2
# #results > li   -> 8
# .item + .item   -> 7
# li.item > a     -> 8


for s in selectors:
    print(s, len(soup.select(s)))

