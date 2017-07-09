'''
Try YOUTUBE-DL
https://github.com/rg3/youtube-dl/blob/master/README.md#embedding-youtube-dl
'''

from __future__ import unicode_literals
import youtube_dl


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
