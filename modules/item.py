import requests
from bs4 import BeautifulSoup
import regex as re
import youtube_dl
import urllib


def search_soup(search):
    urllib.parse.quote(search)
    res = requests.get(
        'https://www.youtube.com/results?search_query={}'.format(search))
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def find_video_(soup):
    length = soup.select('.video-time')
    titles = soup.select('.yt-lockup-video .yt-ui-ellipsis-2.spf-link')
    imgs = soup.select('.contains-addto span.yt-thumb-simple > img')

    l = [{
        'title': el['title'],
        'link': 'https://www.youtube.com{}'.format(el['href'])}
        for el in titles]

    out = list(zip(l, [{'img': a['src']}
                       for a in imgs], [{'length': a.text} for a in length]))
    out = [dict(**ele[0], **ele[1], **ele[2]) for ele in out]

    return out


def page_bar(soup):
    def is_pagination_button(tag):
        return tag.has_attr('aria-label')

    pages_tag = soup.select(
        'a.yt-uix-button.yt-uix-sessionlink.yt-uix-button-default.yt-uix-button-size-default')
    pages = list(filter(is_pagination_button, pages_tag))

    pagination = {page.text: page.get('href') for page in pages}
    return {k: v for (k, v) in pagination.items() if re.match(r'^\d+$', k)}


def download_mp3(url):
    ydl_opts = {
        'outtmpl': 'media/%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp4(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])