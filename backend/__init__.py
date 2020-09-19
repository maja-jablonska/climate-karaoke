import json
import os
from typing import Dict

from flask import Flask, request, abort, send_from_directory
from flask_caching import Cache
from flask_cors import CORS

from .json_utils import simple_message, payload_data
from .youtube_connection import fetch_video_data
from .youtube_connection.youtube_data import YoutubeData
from .youtube_connection.youtube_download import download_from_youtube


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
    @cache.cached(timeout=60)
    def request_song():
        artist_name: str = request.args.get('artist_name', type=str)
        song_name: str = request.args.get('song_name', type=str)
        youtube_data: YoutubeData = fetch_video_data(f'{artist_name} {song_name}')
        return payload_data(youtube_data.to_json())

    @app.route('/download', methods=['GET'])
    def download_song():
        artist_name: str = request.args.get('artist_name', type=str)
        song_name: str = request.args.get('song_name', type=str)
        filename: str = download_from_youtube(artist_name,
                                              song_name,
                                              fetch_video_data(f'{artist_name} {song_name}').video_id)
        print(DOWNLOADS)
        return send_from_directory(DOWNLOADS,
                                   f'{filename.split("/")[-1].replace("webm", "mp3")}')

    return app
