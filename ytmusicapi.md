# YTMusicAPI Reference Methods

## YTMusic Class

### Setup
- **POST** `/api/youtube/setup`
- **POST** `/api/youtube/setup_oauth`

### Search
- **GET** `/api/youtube/search`
- **GET** `/api/youtube/get_search_suggestions`
- **DELETE** `/api/youtube/remove_search_suggestions`

### Browsing
- **GET** `/api/youtube/get_home`
- **GET** `/api/youtube/get_artist/{artistId}`
- **GET** `/api/youtube/get_artist_albums/{artistId}`
- **GET** `/api/youtube/get_album/{albumId}`
- **GET** `/api/youtube/get_album_browse_id/{albumId}`
- **GET** `/api/youtube/get_user`
- **GET** `/api/youtube/get_user_playlists`
- **GET** `/api/youtube/get_user_videos`
- **GET** `/api/youtube/get_song/{songId}`
- **GET** `/api/youtube/get_song_related/{songId}`
- **GET** `/api/youtube/get_lyrics/{songId}`
- **GET** `/api/youtube/get_tasteprofile`
- **POST** `/api/youtube/set_tasteprofile`

### Explore
- **GET** `/api/youtube/get_mood_categories`
- **GET** `/api/youtube/get_mood_playlists`
- **GET** `/api/youtube/get_charts`

### Watch
- **GET** `/api/youtube/get_watch_playlist`

### Library
- **GET** `/api/youtube/get_library_playlists`
- **GET** `/api/youtube/get_library_songs`
- **GET** `/api/youtube/get_library_albums`
- **GET** `/api/youtube/get_library_artists`
- **GET** `/api/youtube/get_library_subscriptions`
- **GET** `/api/youtube/get_library_podcasts`
- **GET** `/api/youtube/get_library_channels`
- **GET** `/api/youtube/get_liked_songs`
- **GET** `/api/youtube/get_saved_episodes`
- **GET** `/api/youtube/get_history`
- **POST** `/api/youtube/add_history_item`
- **DELETE** `/api/youtube/remove_history_items`
- **POST** `/api/youtube/rate_song/{songId}`
- **POST** `/api/youtube/edit_song_library_status/{songId}`
- **POST** `/api/youtube/rate_playlist/{playlistId}`
- **POST** `/api/youtube/subscribe_artists`
- **DELETE** `/api/youtube/unsubscribe_artists`
- **GET** `/api/youtube/get_account_info`

### Playlists
- **GET** `/api/youtube/get_playlist/{playlistId}`
- **POST** `/api/youtube/create_playlist`
- **POST** `/api/youtube/edit_playlist/{playlistId}`
- **DELETE** `/api/youtube/delete_playlist/{playlistId}`
- **POST** `/api/youtube/add_playlist_items/{playlistId}`
- **DELETE** `/api/youtube/remove_playlist_items/{playlistId}`

### Podcasts
- **GET** `/api/youtube/get_channel/{channelId}`
- **GET** `/api/youtube/get_channel_episodes/{channelId}`
- **GET** `/api/youtube/get_podcast/{playlistId}`
- **GET** `/api/youtube/get_episode/{videoId}`
- **GET** `/api/youtube/get_episodes_playlist`

### Uploads
- **GET** `/api/youtube/get_library_upload_songs`
- **GET** `/api/youtube/get_library_upload_artists`
- **GET** `/api/youtube/get_library_upload_albums`
- **GET** `/api/youtube/get_library_upload_artist/{artistId}`
- **GET** `/api/youtube/get_library_upload_album/{albumId}`
- **POST** `/api/youtube/upload_song`
- **DELETE** `/api/youtube/delete_upload_entity/{entityId}`