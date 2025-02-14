from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ytmusicapi import YTMusic, OAuthCredentials
from typing import Any, Literal
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials from environment variables
CLIENT_ID = os.getenv('YOUTUBE_CLIENT_ID')
CLIENT_SECRET = os.getenv('YOUTUBE_CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Missing required environment variables: YOUTUBE_CLIENT_ID and/or YOUTUBE_CLIENT_SECRET")

ytmusic = YTMusic('/etc/secrets/oauth.json', oauth_credentials=OAuthCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/youtube/search/")
async def search(query: str,
                 filter: str | None = None,
                 scope: str | None = None,
                 limit: int = 20,
                 ignore_spelling: bool = False):
    return ytmusic.search(query, filter, scope, limit, ignore_spelling)

@app.get("/api/youtube/get_search_suggestions")
async def get_search_suggestions(query: str,
                                 detailed_runs: bool = False):
    return ytmusic.get_search_suggestions(query, detailed_runs)

@app.delete("/api/youtube/remove_search_suggestions")
async def remove_search_suggestions(suggestions: list[dict[str, Any]],
                                    indices: list[int] | None = None):
    return ytmusic.remove_search_suggestions(suggestions, indices)

@app.get("/api/youtube/get_home")
async def get_home(limit: int = 3):
    return ytmusic.get_home(limit)

@app.get("/api/youtube/get_artist/")
async def get_artist(channelId: str):
    return ytmusic.get_artist(channelId)

@app.get("/api/youtube/get_artist_albums/")
async def get_artist_albums(channelId: str,
                            limit: int | None = 100,
                            order: Literal['Recency', 'Popularity', 'Alphabetical order'] | None = None):
    params = ytmusic.get_artist(channelId)['albums']['params']
    return ytmusic.get_artist_albums(channelId, params, limit, order)

@app.get("/api/youtube/get_album/")
async def get_album(browseId: str):
    return ytmusic.get_album(browseId)

@app.get("/api/youtube/get_album_browse_id/")
async def get_album_browse_id(audioPlaylistId: str):
    return ytmusic.get_album_browse_id(audioPlaylistId)

@app.get("/api/youtube/get_user")
async def get_user(channelId: str):
    return ytmusic.get_user(channelId)

@app.get("/api/youtube/get_user_playlists")
async def get_user_playlists(channelId: str):
    params = ytmusic.get_user(channelId)['playlists']['params']
    return ytmusic.get_user_playlists(channelId, params)

@app.get("/api/youtube/get_user_videos")
async def get_user_videos(channelId: str):
    params = ytmusic.get_user(channelId)['videos']['params']
    return ytmusic.get_user_videos(channelId, params)

@app.get("/api/youtube/get_song/")
async def get_song(videoId: str,
                   signatureTimestamp: int | None = None):
    return ytmusic.get_song(videoId, signatureTimestamp)

@app.get("/api/youtube/get_song_related/")
async def get_song_related(browseId: str):
    return ytmusic.get_song_related(browseId)

@app.get("/api/youtube/get_lyrics/")
async def get_lyrics(browseId: str,
                    timestamps: bool | None = False):
    return ytmusic.get_lyrics(browseId, timestamps)

@app.get("/api/youtube/get_tasteprofile")
async def get_tasteprofile():
    return ytmusic.get_tasteprofile()

@app.post("/api/youtube/set_tasteprofile")
async def set_tasteprofile(artists: list[str], taste_profile: dict | None = None):
    return ytmusic.set_tasteprofile(artists, taste_profile)

@app.get("/api/youtube/get_mood_categories")
async def get_mood_categories():
    return ytmusic.get_mood_categories()

@app.get("/api/youtube/get_mood_playlists")
async def get_mood_playlists(params: str):
    return ytmusic.get_mood_playlists(params)

@app.get("/api/youtube/get_charts")
async def get_charts(country: str = 'ZZ'):
    return ytmusic.get_charts(country)

@app.get("/api/youtube/get_watch_playlist")
async def get_watch_playlist(videoId: str | None = None,
                             playlistId: str | None = None,
                             limit: int = 25,
                             radio: bool = False,
                             shuffle: bool = False):
    return ytmusic.get_watch_playlist(videoId, playlistId, limit, radio, shuffle)

@app.get("/api/youtube/get_library_playlists")
async def get_library_playlists(limit: int | None= 25):
    return ytmusic.get_library_playlists(limit)

@app.get("/api/youtube/get_library_songs")
async def get_library_songs(limit: int = 25,
                            validate_responses: bool = False,
                            order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_songs(limit, validate_responses, order)

@app.get("/api/youtube/get_library_albums")
async def get_library_albums(limit: int | None = 25,
                            order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_albums(limit, order)

@app.get("/api/youtube/get_library_artists")
async def get_library_artists(limit: int | None = 25,
                            order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_artists(limit, order)

@app.get("/api/youtube/get_library_subscriptions")
async def get_library_subscriptions(limit: int | None = 25,
                                    order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_subscriptions(limit, order)

@app.get("/api/youtube/get_library_podcasts")
async def get_library_podcasts(limit: int | None = 25,
                                order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_podcasts(limit, order)

@app.get("/api/youtube/get_library_channels")
async def get_library_channels(limit: int | None = 25,
                                order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_channels(limit, order)

@app.get("/api/youtube/get_liked_songs")
async def get_liked_songs(limit: int = 100):
    return ytmusic.get_liked_songs(limit)

@app.get("/api/youtube/get_saved_episodes")
async def get_saved_episodes(limit: int = 100):
    return ytmusic.get_saved_episodes(limit)

@app.get("/api/youtube/get_history")
async def get_history():
    return ytmusic.get_history()

@app.post("/api/youtube/add_history_item")
async def add_history_item(videoId: str):
    item = ytmusic.get_song(videoId)
    return ytmusic.add_history_item(item)

@app.delete("/api/youtube/remove_history_items")
async def remove_history_items(feedbackTokens: list[str]):
    return ytmusic.remove_history_items(feedbackTokens)

@app.post("/api/youtube/rate_song/")
async def rate_song(videoId: str, rating: str = 'INDIFFERENT'):
    return ytmusic.rate_song(videoId, rating)

@app.post("/api/youtube/edit_song_library_status/")
async def edit_song_library_status(feedbackTokens: list[str] | None = None):
    return ytmusic.edit_song_library_status(feedbackTokens)

@app.post("/api/youtube/rate_playlist/")
async def rate_playlist(playlistId: str, rating: str = 'INDIFFERENT'):
    return ytmusic.rate_playlist(playlistId, rating)

@app.post("/api/youtube/subscribe_artists")
async def subscribe_artists(channelIds: list[str]):
    return ytmusic.subscribe_artists(channelIds)

@app.delete("/api/youtube/unsubscribe_artists")
async def unsubscribe_artists(channelIds: list[str]):
    return ytmusic.unsubscribe_artists(channelIds)

@app.get("/api/youtube/get_account_info")
async def get_account_info():
    return ytmusic.get_account_info()

@app.get("/api/youtube/get_playlist/")
async def get_playlist(playlistId: str,
                       limit: int | None = 100,
                       related: bool = False,
                       suggestions_limit: int = 0):
    return ytmusic.get_playlist(playlistId, limit, related, suggestions_limit)

@app.post("/api/youtube/create_playlist")
async def create_playlist(title: str,
                          description: str,
                          privacy_status: str = 'PRIVATE',
                          video_ids: list[str] | None = None,
                          source_playlist: str | None = None):
    return ytmusic.create_playlist(title, description, privacy_status, video_ids, source_playlist)

@app.post("/api/youtube/edit_playlist/{playlistId}")
async def edit_playlist(playlistId: str,
                        title: str | None = None,
                        description: str | None = None,
                        privacy_status: str | None = None,
                        moveItem: str | tuple[str, str] | None = None,
                        addPlaylistId: str | None = None,
                        addToTop: bool | None = None):
    return ytmusic.edit_playlist(playlistId, title, description, privacy_status, moveItem, addPlaylistId, addToTop)

@app.delete("/api/youtube/delete_playlist/")
async def delete_playlist(playlistId: str):
    return ytmusic.delete_playlist(playlistId)

@app.post("/api/youtube/add_playlist_items/")
async def add_playlist_items(playlistId: str,
                             videoIds: list[str] | None = None,
                             source_playlist: str | None = None,
                             duplicate: bool = False):
    return ytmusic.add_playlist_items(playlistId, videoIds, source_playlist, duplicate)

@app.delete("/api/youtube/remove_playlist_items/")
async def remove_playlist_items(playlistId: str, videos: list[dict]):
    return ytmusic.remove_playlist_items(playlistId, videos)

@app.get("/api/youtube/get_channel/")
async def get_channel(channelId: str):
    return ytmusic.get_channel(channelId)

@app.get("/api/youtube/get_channel_episodes/")
async def get_channel_episodes(channelId: str):
    params = ytmusic.get_channel(channelId)['episodes']['params']
    return ytmusic.get_channel_episodes(channelId, params)

@app.get("/api/youtube/get_podcast/")
async def get_podcast(playlistId: str, limit: int | None = 100):
    return ytmusic.get_podcast(playlistId, limit)

@app.get("/api/youtube/get_episode/")
async def get_episode(videoId: str):
    return ytmusic.get_episode(videoId)

@app.get("/api/youtube/get_episodes_playlist")
async def get_episodes_playlist(playlist_id: str = 'RDPN'):
    return ytmusic.get_episodes_playlist(playlist_id)

@app.get("/api/youtube/get_library_upload_songs")
async def get_library_upload_songs(limit: int | None = 25,
                                   order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_upload_songs(limit, order)

@app.get("/api/youtube/get_library_upload_artists")
async def get_library_upload_artists(limit: int | None = 25,
                                      order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_upload_artists(limit, order)

@app.get("/api/youtube/get_library_upload_albums")
async def get_library_upload_albums(limit: int | None = 25,
                                    order: Literal['a_to_z', 'z_to_a', 'recently_added'] | None = None):
    return ytmusic.get_library_upload_albums(limit, order)

@app.get("/api/youtube/get_library_upload_artist/")
async def get_library_upload_artist(browseId: str,
                                    limit: int = 25):
    return ytmusic.get_library_upload_artist(browseId, limit)

@app.get("/api/youtube/get_library_upload_album/")
async def get_library_upload_album(browseId: str):
    return ytmusic.get_library_upload_album(browseId)

@app.post("/api/youtube/upload_song")
async def upload_song(filepath: str):
    return ytmusic.upload_song(filepath)

@app.delete("/api/youtube/delete_upload_entity/")
async def delete_upload_entity(entityId: str):
    return ytmusic.delete_upload_entity(entityId)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 
