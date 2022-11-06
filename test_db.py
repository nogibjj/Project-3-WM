from spotify_db import SpotifyDB
import os

# test create_db
def test_create_db():
    spotify = SpotifyDB()
    spotify.create_db()
    assert os.path.exists("spotify.db")
