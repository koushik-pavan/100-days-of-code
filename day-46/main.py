import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup


input_date = input("to which date do u want to get transported?(YYYY-MM-DD) ")
#input_date = "2000-08-03"
url = f"https://www.billboard.com/charts/hot-100/{input_date}"
response = requests.get(url=url)
data = response.text
soup = BeautifulSoup(data, "html.parser")
titles = soup.select("li ul li h3")
titles = [i.getText().strip() for i in titles]
artist_uri = []
year = input_date.split("-")[0]
#auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id = '65f5acbf8ebd4429a9af15a7b6c6aa92', scope="playlist-modify-private", client_secret = '110f4962d78649d4ba3b18b49f25fb32', redirect_uri = 'http://127.0.0.1:9090', show_dialog=True, username="PAVAN KOUSHIK VADDADI"))
for name in titles:
    results = sp.search(q=f"track:{name} year:{year}", type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        artist_uri.append(uri)
    except:
        print("skipped the song")
user_id = sp.current_user()['id']
my_playlist = sp.user_playlist_create(user= user_id, name=f"BillBoard100", public=False)
#user_playlist_add_tracks
sp.playlist_add_items(playlist_id=my_playlist["id"], items=artist_uri)