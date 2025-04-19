import requests
import subprocess
import os

# Client Details from Spotify for Developers

CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Function for generating a Access Token
def get_access_code(clientID,clientSecret):
    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": clientID,
        "client_secret": clientSecret
    }

    response = requests.post(url,headers=headers,data=data)

    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        print("Error:", response.status_code, response.text)
        return None
    
current_token = get_access_code(CLIENT_ID,CLIENT_SECRET)

# Function to get your playlists, Add your spotify username in the "username" variable
def get_my_playlists(access_token):

    current_playlist = {}

    username = "YOUR_USER_NAME" 

    url = f"https://api.spotify.com/v1/users/{username}/playlists"

    header = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url,headers=header)

    if response.status_code == 200:
        data = response.json().get('items', [])
        #print(data)
        for playlist in data:
            name = playlist.get('name')
            url = playlist.get('external_urls', {}).get('spotify')
            if name and url:
                current_playlist[name] = url
        return current_playlist


    elif response.status_code == 401:
        current_token = get_access_code(CLIENT_ID,CLIENT_SECRET)
        get_my_playlists(current_token)
    else:
        error = response.json()['error'] 
        print(error)

current_playlist = get_my_playlists(current_token)

#print(current_playlist)


# Function for downloading your songs by playlists, Specify the output path in code
def download_playlist(playlist):
    for name, url in current_playlist.items():
        print(f"Downloading playlist: {name}")
        subprocess.run(["python", "-m", "spotdl", url, "--output", f"Pass1/{name}"])
        

download_playlist(current_playlist)