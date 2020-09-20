import json
import os
import moviepy.editor as mp
from typing import Dict

from flask import Flask, request, abort, send_from_directory
from flask_caching import Cache
from flask_cors import CORS, cross_origin

from .json_utils import simple_message, payload_data
from .youtube_connection import fetch_video_data
from .youtube_connection.youtube_data import YoutubeData
from .youtube_connection.youtube_download import download_from_youtube
from .vocal_split import split_vocals
from .genius_connection import query_genius
from .lyrics_generation import *


DOWNLOADS: str = os.path.dirname(os.path.realpath(__file__))+'/../downloads/'


def read_json_configuration() -> Dict[str, str]:
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/configuration.json') as conf:
        return json.load(conf)


def create_app() -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    configuration: Dict[str, str] = read_json_configuration()
    app.config.from_mapping()

    cache = Cache(config={'CACHE_TYPE': 'simple'})
    CORS(app)
    cache.init_app(app)

    @app.route('/')
    def index():
        return simple_message('Welcome to climate karaoke!')

    @app.route('/song', methods=['GET'])
    @cross_origin()
    @cache.cached()
    def request_song():
        artist_name: str = request.args.get('artist_name', type=str)
        song_name: str = request.args.get('song_name', type=str)
        youtube_data: YoutubeData = fetch_video_data(f'{artist_name} {song_name}')
        return payload_data(youtube_data.to_json())

    @app.route('/download', methods=['GET'])
    @cross_origin()
    def download_song():
        artist_name: str = request.args.get('artist_name', type=str)
        song_name: str = request.args.get('song_name', type=str)
        filename: str = download_from_youtube(artist_name,
                                              song_name,
                                              fetch_video_data(f'{artist_name} {song_name}').video_id)
        accompaniament_path, accompaniament_filename = split_vocals(filename.replace("webm", "mp3"))
        print(accompaniament_path)
        return send_from_directory(accompaniament_path,
                                   accompaniament_filename)

    @app.route('/lyrics', methods=['GET'])
    @cross_origin()
    def request_lyrics():
        song_name: str = request.args.get('song_name', type=str)
        genius_data = query_genius(song_name)
        return genius_data.to_json()
    return app
