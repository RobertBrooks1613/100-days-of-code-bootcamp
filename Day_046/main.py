from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

client_id = 'you-client-id'
client_secret = 'your-client-secret'
redirect_uri = 'http://localhost:8888/callback'
scope = "playlist-modify-public"

# Set up SpotifyOAuth
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope)

# Get the authorization URL and open it in the browser
auth_url = sp_oauth.get_authorize_url()
print(f'Please navigate here: {auth_url}')
webbrowser.open(auth_url)

# Wait for user to authorize and get the code from the redirect URL
response = input('Enter the URL you were redirected to: ')

# Extract the code from the response
code = sp_oauth.parse_response_code(response)

# Get the access token
token_info = sp_oauth.get_access_token(code)

# Create the Spotify client
sp = spotipy.Spotify(auth=token_info['access_token'])

# Get user info
user_info = sp.me()
user_id = user_info['id']
print(f"Successfully authenticated. User ID: {user_id}")

# Take user input YYYY-MM-DD
user_input = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

# Connect to billboard and scrape site for a playlist based off user input
content = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}", 
                       headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"})
soup = BeautifulSoup(content.text, "html.parser")

get_container = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in get_container]

playlist_name = f"Top 100 songs from {user_input}"

# Create a new playlist
playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
playlist_id = playlist['id']
print(f"Created playlist: {playlist_name}")

# List to store track URIs
track_uris = []

for i, song_name in enumerate(song_names):
    print(f"Searching for: {i + 1}: {song_name}")
    
    # Search for the track
    result = sp.search(q=song_name, type='track', limit=1)
    
    # Check if we found a matching track
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        track_uri = track['uri']
        track_uris.append(track_uri)
        print(f"Found: {track['name']} by {track['artists'][0]['name']}")
    else:
        print(f"Could not find a match for: {song_name}")

# Add all found tracks to the playlist
if track_uris:
    # Add tracks in batches of 100 (Spotify API limit)
    for i in range(0, len(track_uris), 100):
        batch = track_uris[i:i+100]
        sp.playlist_add_items(playlist_id, batch)
    print(f"Added {len(track_uris)} tracks to the playlist '{playlist_name}'")
else:
    print("No tracks were found to add to the playlist.")