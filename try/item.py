import re
import requests
from bs4 import BeautifulSoup


def find_search_content(search_text):

    search_text = re.sub(r'\s', '', search_text)

    res = requests.get(
        'https://www.youtube.com/results?search_query={}'.format(search_text))
    soup = BeautifulSoup(res.content, 'lxml')

    return soup


def find_video_info_(soup):
    titles = soup.select('.yt-lockup-video .yt-ui-ellipsis-2.spf-link')
    imgs = soup.select('.contains-addto img')
    imgs[0]['src']

    l = [{
        'title': el['title'],
        'link': el['href']}
        for el in titles]

    video_time = soup.select('.video-time')
    out = list(zip(l,
                   [{'img': a['src']} for a in imgs],
                   [{'video_time': a.text} for a in video_time]))
    out = [dict(**ele[0], **ele[1], **ele[2]) for ele in out]

    return out







