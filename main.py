from fastapi import FastAPI, HTTPException
from prisma import Prisma
from typing import Dict, List, Any
import logging
from contextlib import asynccontextmanager
from ytmusic import get_artist, get_artist_albums, get_album, get_playlist

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events."""
    await prisma.connect()
    logger.info("Connected to database")
    yield
    await prisma.disconnect()
    logger.info("Disconnected from database")

app = FastAPI(lifespan=lifespan)
prisma = Prisma()

async def create_or_update_artist(artist_id: str, artist_data: Dict[str, Any]) -> None:
    """Create or update an artist record in the database.
    
    Args:
        artist_id: The YouTube channel ID of the artist
        artist_data: Dictionary containing artist information
    """
    logger.info(f"Creating/updating artist: {artist_data['name']} ({artist_id})")
    await prisma.artist.upsert(
        where={'id': artist_id},
        data={
            'create': {
                'id': artist_id,
                'name': artist_data['name']
            },
            'update': {
                'name': artist_data['name']
            }
        }
    )
    logger.info(f"Successfully processed artist: {artist_data['name']}")

async def process_album_tracks(album_id: str, tracks: List[Dict[str, Any]], artist_id: str) -> None:
    """Process and store tracks from an album.
    
    Args:
        album_id: The album's browseId
        tracks: List of track information
        artist_id: The artist's channel ID
    """
    logger.info(f"Processing {len(tracks)} tracks for album {album_id}")
    for track in tracks:
        try:
            await prisma.song.upsert(
                where={'id': track['videoId']},
                data={
                    'create': {
                        'id': track['videoId'],
                        'title': track['title'],
                        'duration': track['duration_seconds'],
                        'artistId': artist_id,
                        'albumId': album_id
                    },
                    'update': {
                        'title': track['title'],
                        'duration': track['duration_seconds']
                    }
                }
            )
            logger.debug(f"Processed track: {track['title']}")
        except Exception as e:
            logger.error(f"Error processing track {track['title']}: {str(e)}")
            raise

async def process_album(album_data: Dict[str, Any], artist_id: str) -> None:
    """Process and store an album and its tracks.
    
    Args:
        album_data: Dictionary containing album information
        artist_id: The artist's channel ID
    """
    album_title = album_data['title'].replace(' - Topic', '')
    logger.info(f"Processing album: {album_title}")

    # Clean album data
    album_data['title'] = album_title
    album_data['year'] = album_data['year'] if album_data['year'] != 'Unreleased' else None
    
    try:
        # Create or update album
        await prisma.album.upsert(
            where={'id': album_data['browseId']},
            data={
                'create': {
                    'id': album_data['browseId'],
                    'title': album_data['title'],
                    'year': album_data['year'],
                    'artistId': artist_id
                },
                'update': {
                    'title': album_data['title'],
                    'year': album_data['year']
                }
            }
        )
        logger.info(f"Successfully stored album: {album_title}")

        # Fetch and process album tracks
        logger.info(f"Fetching tracks for album: {album_title}")
        album = get_album(album_data['browseId'])

        
        await process_album_tracks(album_data['browseId'], album['tracks'], artist_id)
        logger.info(f"Completed processing album: {album_title}")
    except Exception as e:
        logger.error(f"Error processing album {album_title}: {str(e)}")
        raise

async def process_loose_tracks(tracks: List[Dict[str, Any]], artist_id: str) -> None:
    """Process and store tracks that aren't associated with any album.
    
    Args:
        tracks: List of track information
        artist_id: The artist's channel ID
    """
    logger.info(f"Processing {len(tracks)} loose tracks")
    processed_count = 0
    error_count = 0

    for track in tracks:
        try:
            await prisma.song.upsert(
                where={'id': track['videoId']},
                data={
                    'create': {
                        'id': track['videoId'],
                        'title': track['title'],
                        'duration': track['duration_seconds'],
                        'artistId': artist_id
                    },
                    'update': {
                        'title': track['title'],
                        'duration': track['duration_seconds']
                    }
                }
            )
            processed_count += 1
            logger.debug(f"Processed loose track: {track['title']}")
        except Exception as e:
            error_count += 1
            logger.error(f"Error processing loose track {track['title']}: {str(e)}")
    
    logger.info(f"Completed processing loose tracks. Successful: {processed_count}, Failed: {error_count}")

@app.get("/scrape/{artist_id}")
async def scrape_artist(artist_id: str):
    """Endpoint to scrape and store artist data from YouTube Music."""
    logger.info(f"Starting scrape for artist ID: {artist_id}")

    try:
        # Fetch artist details using the ytmusic methods
        artist_data = get_artist(artist_id)
        logger.info(f"Found artist: {artist_data['name']}")

        # Create or update artist record
        await create_or_update_artist(artist_id, artist_data)

        # Process albums
        albums = get_artist_albums(artist_data['albums']['browseId'], artist_data['albums']['params'])
        logger.info(f"Found {len(albums)} albums")

        for album in albums:
            await process_album(album, artist_id)

        # Process singles
        singles = get_artist_albums(artist_data['singles']['browseId'], artist_data['singles']['params'])
        logger.info(f"Found {len(singles)} singles")

        for single in singles:
            await process_album(single, artist_id)
        
        # Process library songs
        songs_data = get_playlist(artist_data['songs']['browseId'])
        logger.info(f"Found {len(songs_data['tracks'])} loose songs")
        await process_loose_tracks(songs_data['tracks'], artist_id)

        return {"message": f"Successfully scraped and stored data for artist {artist_id}"}

    except Exception as e:
        logger.error(f"Error processing artist {artist_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing artist {artist_id}: {str(e)}")
    