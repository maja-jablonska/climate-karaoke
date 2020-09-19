from __future__ import unicode_literals
from pytube import YouTube
import os


YOUTUBE_WATCH_STRING: str = "https://www.youtube.com/watch?v="
SAVE_PATH = os.getcwd() + '/downloads/'


def download_from_youtube(artist_name: str, song_name: str, video_id: str):
    yt: YouTube = YouTube(f'{YOUTUBE_WATCH_STRING}{video_id}')
    ys = yt.streams.filter(file_extension='mp4').get_lowest_resolution()
    filename: str = f'{artist_name}_{song_name}'
    ys.download(SAVE_PATH, filename=filename)
    return f'{SAVE_PATH}{filename}.mp4'
