from spotify_db import SpotifyDB
import sqlite3
import pandas as pd
import pytest
import os
import sys
import fire

# test create_db
def test_create_db():
    spotify = SpotifyDB()
    spotify.create_db()
    assert os.path.exists("spotify.db")
