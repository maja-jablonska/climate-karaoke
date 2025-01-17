# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from typing import Sequence

from .youtube_data import YoutubeData

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=os.environ["YOUTUBE_API_KEY"])
def fetch_video_data(query: str) -> YoutubeData:
    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=query
    )
    response = request.execute()
    return YoutubeData(response, 0)