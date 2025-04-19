import requests
import subprocess

# Client Details from Spotify for Developers

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

test_playlist = {
    'Chowrasta & Co.': 'https://open.spotify.com/playlist/63XbvaB2I6BNkaQm0m1ota',
    'Leader': 'https://open.spotify.com/playlist/5yXeVOWrdnR8HUJ3JxixCR'
}

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
        #print(token)
        return token
    else:
        print("Error:", response.status_code, response.text)
        return None
    
current_token = get_access_code(CLIENT_ID,CLIENT_SECRET)

def get_my_playlists(access_token):

    current_playlist = {}

    url = "https://api.spotify.com/v1/users/31xiaxyocyddcrtajcdoxhaeaysa/playlists"

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
print(current_playlist)

def download_playlist(playlist):
    for name, url in current_playlist.items():
        print(f"Downloading playlist: {name}")
        subprocess.run(["python", "-m", "spotdl", url, "--output", f"Pass1/{name}"])
        

download_playlist(current_playlist)