import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.youtube.com/results?search_query=john+mayer')
soup = BeautifulSoup(res.content, 'lxml')

titles = soup.select('.yt-lockup-video .yt-ui-ellipsis-2.spf-link')
print(titles)
