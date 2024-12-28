from fastapi import FastAPI, HTTPException
from ytmusicapi import YTMusic
from typing import Any, Literal

app = FastAPI()
ytmusic = YTMusic()

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
    params = ytmusic.get_mood_categories()['playlists']['params']
    return ytmusic.get_mood_playlists(params)

@app.get("/api/youtube/get_charts")
async def get_charts():
    return ytmusic.get_charts()

@app.get("/api/youtube/get_watch_playlist")
async def get_watch_playlist():
    return ytmusic.get_watch_playlist()

@app.get("/api/youtube/get_library_playlists")
async def get_library_playlists():
    return ytmusic.get_library_playlists()

@app.get("/api/youtube/get_library_songs")
async def get_library_songs():
    return ytmusic.get_library_songs()

@app.get("/api/youtube/get_library_albums")
async def get_library_albums():
    return ytmusic.get_library_albums()

@app.get("/api/youtube/get_library_artists")
async def get_library_artists():
    return ytmusic.get_library_artists()

@app.get("/api/youtube/get_library_subscriptions")
async def get_library_subscriptions():
    return ytmusic.get_library_subscriptions()

@app.get("/api/youtube/get_library_podcasts")
async def get_library_podcasts():
    return ytmusic.get_library_podcasts()

@app.get("/api/youtube/get_library_channels")
async def get_library_channels():
    return ytmusic.get_library_channels()

@app.get("/api/youtube/get_liked_songs")
async def get_liked_songs():
    return ytmusic.get_liked_songs()

@app.get("/api/youtube/get_saved_episodes")
async def get_saved_episodes():
    return ytmusic.get_saved_episodes()

@app.get("/api/youtube/get_history")
async def get_history():
    return ytmusic.get_history()

@app.post("/api/youtube/add_history_item")
async def add_history_item(item: dict):
    return ytmusic.add_history_item(item)

@app.delete("/api/youtube/remove_history_items")
async def remove_history_items(items: list):
    return ytmusic.remove_history_items(items)

@app.post("/api/youtube/rate_song/{songId}")
async def rate_song(songId: str, rating: int):
    return ytmusic.rate_song(songId, rating)

@app.post("/api/youtube/edit_song_library_status/{songId}")
async def edit_song_library_status(songId: str, status: str):
    return ytmusic.edit_song_library_status(songId, status)

@app.post("/api/youtube/rate_playlist/{playlistId}")
async def rate_playlist(playlistId: str, rating: int):
    return ytmusic.rate_playlist(playlistId, rating)

@app.post("/api/youtube/subscribe_artists")
async def subscribe_artists(artistIds: list):
    return ytmusic.subscribe_artists(artistIds)

@app.delete("/api/youtube/unsubscribe_artists")
async def unsubscribe_artists(artistIds: list):
    return ytmusic.unsubscribe_artists(artistIds)

@app.get("/api/youtube/get_account_info")
async def get_account_info():
    return ytmusic.get_account_info()

@app.get("/api/youtube/get_playlist/{playlistId}")
async def get_playlist(playlistId: str):
    return ytmusic.get_playlist(playlistId)

@app.post("/api/youtube/create_playlist")
async def create_playlist(title: str):
    return ytmusic.create_playlist(title)

@app.post("/api/youtube/edit_playlist/{playlistId}")
async def edit_playlist(playlistId: str, data: dict):
    return ytmusic.edit_playlist(playlistId, data)

@app.delete("/api/youtube/delete_playlist/{playlistId}")
async def delete_playlist(playlistId: str):
    return ytmusic.delete_playlist(playlistId)

@app.post("/api/youtube/add_playlist_items/{playlistId}")
async def add_playlist_items(playlistId: str, items: list):
    return ytmusic.add_playlist_items(playlistId, items)

@app.delete("/api/youtube/remove_playlist_items/{playlistId}")
async def remove_playlist_items(playlistId: str, items: list):
    return ytmusic.remove_playlist_items(playlistId, items)

@app.get("/api/youtube/get_channel/{channelId}")
async def get_channel(channelId: str):
    return ytmusic.get_channel(channelId)

@app.get("/api/youtube/get_channel_episodes/{channelId}")
async def get_channel_episodes(channelId: str, params: str):
    return ytmusic.get_channel_episodes(channelId, params)

@app.get("/api/youtube/get_podcast/{playlistId}")
async def get_podcast(playlistId: str, limit: int = 100):
    return ytmusic.get_podcast(playlistId, limit)

@app.get("/api/youtube/get_episode/{videoId}")
async def get_episode(videoId: str):
    return ytmusic.get_episode(videoId)

@app.get("/api/youtube/get_episodes_playlist")
async def get_episodes_playlist(playlist_id: str = 'RDPN'):
    return ytmusic.get_episodes_playlist(playlist_id)

@app.get("/api/youtube/get_library_upload_songs")
async def get_library_upload_songs():
    return ytmusic.get_library_upload_songs()

@app.get("/api/youtube/get_library_upload_artists")
async def get_library_upload_artists():
    return ytmusic.get_library_upload_artists()

@app.get("/api/youtube/get_library_upload_albums")
async def get_library_upload_albums():
    return ytmusic.get_library_upload_albums()

@app.get("/api/youtube/get_library_upload_artist/{artistId}")
async def get_library_upload_artist(artistId: str):
    return ytmusic.get_library_upload_artist(artistId)

@app.get("/api/youtube/get_library_upload_album/{albumId}")
async def get_library_upload_album(albumId: str):
    return ytmusic.get_library_upload_album(albumId)

@app.post("/api/youtube/upload_song")
async def upload_song(song_data: dict):
    return ytmusic.upload_song(song_data)

@app.delete("/api/youtube/delete_upload_entity/{entityId}")
async def delete_upload_entity(entityId: str):
    return ytmusic.delete_upload_entity(entityId)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
