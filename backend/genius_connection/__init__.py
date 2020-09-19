import lyricsgenius
from .genius_data import GeniusData

access_token = "mCYmlsEw8dyYF7VD3WGF7wj9qHnAceG6_tmRQ2BU-6mP1Ced58nKR5uLBJcQL3Ko"

genius = lyricsgenius.Genius(access_token)

def query_genius(query: str) -> str:

    song = genius.search_song(query)

    return GeniusData(song)


