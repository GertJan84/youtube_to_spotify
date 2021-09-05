import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self, CLIENT_ID, CLIENT_SEC):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SEC, redirect_uri="http://example.com", scope="playlist-modify-private", show_dialog=True, cache_path="token.txt"))
        self.user_id = self.sp.current_user()["id"]

    def find_songs(self, artist, track):
        result = self.sp.search(q=f"track:{track} artist:{artist}", type="track")

        results = result["tracks"]['items']

        if results:
            uri = result["tracks"]["items"][0]["uri"]
            if not uri == None:
                return uri
        else:
            print(f"No song found for {artist} = {track}")

        

    def add_songs_to_spotify(self, song_uris):
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"python test", public=False)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)