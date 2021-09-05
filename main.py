from dotenv import load_dotenv
from Get_Youtube_Data import Youtube
from Spotify_module import Spotify
import os

# Load .env file
load_dotenv()

# Set variable from the items in .env file
API_KEY = os.environ.get("API_KEY")
CLIENT_ID = os.environ.get("S_CLIENT_ID")
CLIENT_SEC = os.environ.get("S_CLIENT_SEC")

# Ask for youtube url
youtube_url = input("Enter youtube url: ")

# Initilise modules
youtube = Youtube(API_KEY)
spotify = Spotify(CLIENT_ID, CLIENT_SEC)

# Get youtube titles
songs = youtube.get_playlist_items(youtube_url)

# Get Spotify uri
song_uris = [spotify.find_songs(song.artist, song.track) for song in songs]

# Remove None from spotify uri list
song_uris = [song for song in song_uris if not song == None]

# Create playlist and add songs to it
spotify.add_songs_to_spotify(song_uris)