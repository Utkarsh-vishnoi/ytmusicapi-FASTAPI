from ytmusicapi import YTMusic, OAuthCredentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load environment variables
CLIENT_ID = os.getenv('YOUTUBE_CLIENT_ID')
CLIENT_SECRET = os.getenv('YOUTUBE_CLIENT_SECRET')
OAUTH_FILE = os.getenv('OAUTH_FILE')

if not all([CLIENT_ID, CLIENT_SECRET, OAUTH_FILE]):
    raise ValueError("Missing required environment variables")

ytmusic = YTMusic(OAUTH_FILE, oauth_credentials=OAuthCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

def get_artist(channelId: str):
    return ytmusic.get_artist(channelId)

def get_artist_albums(browseId: str, params: str, limit: int = 1000, order: str = None):
    return ytmusic.get_artist_albums(browseId, params, limit, order)

def get_album(browseId: str):
    return ytmusic.get_album(browseId)

def get_playlist(playlistId: str, limit: int = 1000):
    return ytmusic.get_playlist(playlistId, limit)

# Add more methods as needed...