from modules import item

search = 'john mayer'
soup = item.search_soup(search)
res = item.find_video_(soup)

for item in res:
    print(item.get('title'), item.get('img'))

