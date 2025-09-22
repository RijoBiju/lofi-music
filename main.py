from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/spotify-playlist")
async def get_spotify_playlist_details(playlist_id: str = Query(...)):
    from app.spotify_client import get_playlist, get_track_from_playlist, get_artists_from_playlist, get_track_image
    from app.youtube_search import search_youtube
    playlist = get_playlist(playlist_id)
    artist, track, image = get_artists_from_playlist(playlist[0]), get_track_from_playlist(playlist[0]), get_track_image(playlist[0])
    search_result = search_youtube(query=f"{artist} {track}")
    # return {'album_art': image, 'artist': artist, 'track': track}
    return search_result