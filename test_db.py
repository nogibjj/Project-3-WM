from spotify_db import SpotifyDB
import sqlite3
import pandas as pd
import pytest
import os
import sys
import fire

# Create a test database
def test_create_db():
    spotify = SpotifyDB()
    spotify.create_db()
    assert os.path.exists('spotify.db'), "The database was not created"
    conn = sqlite3.connect("spotify.db")
    cnc = conn.cursor()
    cnc.execute("SELECT * FROM spotify LIMIT 10")
    assert len(cnc.fetchall()) == 10, "The number of rows is not correct"
    conn.commit()
    conn.close()
    