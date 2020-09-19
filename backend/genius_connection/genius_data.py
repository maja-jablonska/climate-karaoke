import lyricsgenius
from typing import Sequence
import re

class GeniusData:
    def __init__(self, song_data: lyricsgenius.song):
        self.__title: str = song_data.title
        self.__lyrics: Sequence[str] = self.parse_lyrics(song_data.lyrics)

    @property
    def title(self) -> str:
        return self.__title

    @property
    def lyrics(self) -> Sequence[str]:
        return self.__lyrics

    def parse_lyrics(self, lyrics: str) -> Sequence[str]:
        lyrics_without_comments = re.sub("[.*?]", "", lyrics)
        splitted_lyrics = lyrics_without_comments.split("\n")
        filtered_lyrics = [line for line in splitted_lyrics if '[' not in line and ']' not in line]
        return filtered_lyrics

    def to_json(self):
        return {
            'song': self.__title,
            'lyrics': self.__lyrics
        }

