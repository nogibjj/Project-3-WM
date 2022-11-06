import fire
import sqlite3
import pandas as pd


class SpotifyDB:
    def create_db(self):
        """Creates a database with a table called 'spotify'
        :param: df: pandas dataframe"""
        conn = sqlite3.connect("spotify.db")
        df = pd.read_csv("spotify_dataset.csv")
        df.to_sql("spotify", conn, if_exists="replace", index=False)
        print('Database created')
        conn.commit()
        conn.close()

    def query10(self):
        """Returns 10 first rows of the table"""
        conn = sqlite3.connect("spotify.db")
        cnc = conn.cursor()
        cnc.execute("SELECT * FROM spotify LIMIT 10")
        print(cnc.fetchall())
        conn.commit()
        conn.close()


# run the CLI
if __name__ == "__main__":
    spotify = SpotifyDB()
    fire.Fire(spotify)
