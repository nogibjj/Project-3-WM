import sqlite3
import fire

class askspotify:
    def avg_length_top_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT AVG(duration_ms)/60000 FROM spotify WHERE popularity > 90;")
        popsong = cnc.fetchall()
        print(f"The average length of a popular song is {popsong[0][0]:.2f} minutes.")

    def avg_length_unpopular_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT AVG(duration_ms)/60000 FROM spotify WHERE popularity < 10;")
        nonpopsong = cnc.fetchall()
        print(f"The average length of a non popular song is {nonpopsong[0][0]:.2f} minutes.")

    def dance_score_top_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT AVG(danceability) FROM spotify WHERE popularity > 90;")
        popdance = cnc.fetchall()
        print(f"The average danceability of a popular song is {popdance[0][0]:.2f}.")

    def dance_score_unpopular_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT AVG(danceability) FROM spotify WHERE popularity < 100;")
        nonpopdance = cnc.fetchall()
        print(f"The average danceability of a non popular song is {nonpopdance[0][0]:.2f}.")

    def top_10_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT DISTINCT(track_name), artists, popularity FROM spotify ORDER BY popularity DESC LIMIT 10;")
        top10 = cnc.fetchall()
        print(f"The top 10 most popular songs are: {top10}")

    def bottom_10_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT DISTINCT(track_name), artists, popularity FROM spotify ORDER BY popularity ASC LIMIT 10;")
        bottom10 = cnc.fetchall()
        print(f"The top 10 least popular songs are: {bottom10}")

    def top_10_live_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT DISTINCT(track_name), artists, liveness, popularity FROM spotify WHERE popularity > 80 ORDER BY liveness DESC LIMIT 10;")
        live10 = cnc.fetchall()
        print(f"The top 10 live songs are: {live10}")

    def top_10_studio_songs(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT DISTINCT(track_name), artists, liveness, popularity FROM spotify WHERE popularity > 80 ORDER BY liveness ASC LIMIT 10;")
        nonlive10 = cnc.fetchall()
        print(f"The top 10 non live songs are: {nonlive10}")

    def top_10_albums(self):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        # sum of popularity of all songs in an album / number of songs in album
        cnc.execute("SELECT DISTINCT(album_name), artists, SUM(popularity)/COUNT(popularity) FROM spotify GROUP BY album_name ORDER BY SUM(popularity)/COUNT(popularity) DESC LIMIT 10;")
        album10 = cnc.fetchall()
        # print(f"The albums with the highest total song popularity are: {print(i[0]) for i in album10}")
        print(print(item[0][0]) for item in album10)

    def my_fav_band(self, band):
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute(f"SELECT DISTINCT(track_name), artists, popularity FROM spotify WHERE artists LIKE '%{band}%' ORDER BY popularity DESC LIMIT 10;")
        band10 = cnc.fetchall()
        print(f"The top 10 most popular songs by {band} are: {band10}")

if __name__ == "__main__":
    spotify = askspotify()
    fire.Fire(spotify)
