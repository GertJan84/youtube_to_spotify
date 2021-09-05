from googleapiclient.discovery import build
import youtube_dl

var_maxResults = 100

class Song:
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track
        

class Youtube:
    def __init__(self, api_key):
        # Initilize youtube api
        self.client = build('youtube', 'v3', developerKey=api_key)

    def get_artist_and_track(self, video_id):
        youtube_url = f"https://youtube.com/watch?v={video_id}"

        try:
            video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
                youtube_url, download=False
            )
        except youtube_dl.utils.DownloadError:
            video = False
            pass

        try:
            track = video['track']
            artist = video['artist']
        except:
            track = False
            artist = False
            pass

        return artist, track

    def get_playlist_items(self, url):

        # Get playlist id
        playlist_id =  str(url.split("&")[1].split("list=")[1])

        # Setup request
        request = self.client.playlistItems().list(
            part="id, snippet",
            maxResults=var_maxResults,
            playlistId=playlist_id
        )

        # Execute request
        response = request.execute()

        songs = []
        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            artist, track = self.get_artist_and_track(video_id)
            if artist and track:
                songs.append(Song(artist, track))

        return songs




        
