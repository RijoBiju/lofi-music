import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_playlist(playlist_id):
    playlist = sp.playlist(playlist_id)
    return playlist["tracks"]["items"]

def get_artists_from_playlist(playlist_response):
    return playlist_response["track"]["artists"][0]["name"]

def get_track_from_playlist(playlist_response):
    return playlist_response["track"]["name"]

def get_track_image(playlist_response):
    return playlist_response["track"]["album"]["images"][0]["url"]
