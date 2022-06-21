import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "7c02b6487085453792eb165090f496bd"
SPOTIFY_SECRET = "627363047d914d70a4d2632601641c35"
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

DAY = input("Witch year do you want to travel? Type the data in this format YYYY-MM-DD\n")
URL_LIST = f"https://www.billboard.com/charts/hot-100/{DAY}/"

response = requests.get(url=URL_LIST)
soup = BeautifulSoup(response.text, "html.parser")
all_songs_data = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
songs_name = [song.getText().strip() for song in all_songs_data]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=f"{SPOTIFY_ID}",
        client_secret=f"{SPOTIFY_SECRET}",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

uri = sp.search(q=f"track:{songs_name[0]}", type="track")
print(uri)

print(user_id)






