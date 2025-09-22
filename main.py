from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/spotify-playlist")
async def get_spotify_playlist_details(playlist_id: str = Query(...)):
    from app.spotify_client import get_playlist, get_track_from_playlist, get_artists_from_playlist, get_track_image
    playlist = get_playlist(playlist_id)
    artist, track, image = get_artists_from_playlist(playlist[0]), get_track_from_playlist(playlist[0]), get_track_image(playlist[0])
    return {'album_art': image, 'artist': artist, 'track': track}