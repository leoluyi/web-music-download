import sys
from os.path import abspath, join, dirname, pardir
sys.path.insert(0, (abspath(join(dirname(__file__), pardir))))
# print(sys.path)

from modules import item

search = 'john mayer'
soup = item.search_soup(search)
res = item.find_video_(soup)

for i in res:
    print(i.get('title') + '===>' + i.get('img'))
