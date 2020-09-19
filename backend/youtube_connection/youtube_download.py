from __future__ import unicode_literals
import youtube_dl
import os


YOUTUBE_WATCH_STRING: str = "https://www.youtube.com/watch?v="
SAVE_PATH = os.getcwd() + '/downloads/'


def my_hook(d):
    global FILENAME
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    FILENAME = d['filename']


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [my_hook],
    'outtmpl': SAVE_PATH + '%(title)s.%(ext)s'
}


def download_from_youtube(artist_name: str, song_name: str, video_id: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'{YOUTUBE_WATCH_STRING}{video_id}'])
        return FILENAME
