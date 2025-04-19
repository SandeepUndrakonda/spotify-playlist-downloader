# Spotify Playlist Downloader

> *This script uses the Spotify Web API along with the awesome [**spotDL**](https://github.com/spotDL/spotify-downloader.git) tool to help you download all the songs from your public Spotify playlists.
All you need to do is add your Client ID, Client Secret, and your Spotify username and it’ll take care of the rest. It fetches all your playlists and downloads the songs, keeping them nicely organized in folders by playlist name.*
## Features
- 🔐 Uses Spotify Web API with your own credentials (Client ID & Secret)
- 👤 Fetches all public playlists for a given Spotify username
- 🎶 Automatically downloads all songs from those playlists
- 📁 Organizes downloaded songs into folders named after each playlist
- ⚙️ Works seamlessly with spotDL to handle song downloads
- 💡 Easy to set up using environment variables
- 🧩 Minimal setup, no need for user authentication or complex login flows
## Requirements
Make sure the following are installed and properly set up:
- Python 3.7 or higher (Added To Path)
- Spotdl [*Installation Instructions*](https://spotdl.readthedocs.io/en/latest/installation/)
- FFmpeg 4.2 [*Installation Instructions*](https://spotdl.readthedocs.io/en/latest/installation/)
>Run `spotdl --download-ffmpeg` to download FFmpeg for the SpotDL folder after installation.
## Installation
1. Guidlines
    - Make sure all required dependencies are installed correctly.
    - Choose a folder to store the downloaded songs, as the code uses a relative folder structure for output.
2. Clone the repository
    - Open Terminal or CMD in the folder where you want your playlists to be saved.
    - Step 1: `git clone https://github.com/SandeepUndrakonda/spotify-playlist-downloader.git`
    - Step 2: `cd spotify-playlist-downloader`
3. Create a Spotify Developer App
    - Follow this guide to create an app and get your Client ID and Client Secret:
[Spotify Developer Guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
4. Set Up Environment Variables
    - For better security, add Client ID and Client Secret as environment variables:
    - Open Edit System Environment Variables and add:
        - SPOTIFY_CLIENT_ID = your Client ID
        - SPOTIFY_CLIENT_SECRET = your Client Secret
    - Alternatively, you can directly paste them in the code:
    ```python
    CLIENT_ID = "your-client-id"
    CLIENT_SECRET = "your-client-secret"
    ```
5. Set Your Spotify Username
    - Find your Spotify username here: Spotify Account Profile
    - Copy your username and paste it into the code under the get_my_playlists function:
    ```python
    username = "your-username"
    ```
6. Choose Your Download Folder
    - The code uses the folder "Pass1" for storing downloads. You can change this to any folder name you prefer:
    ```python
    subprocess.run(["python", "-m", "spotdl", url, "--output", f"Pass1/{name}"])
    ```
7. Run the Script
    - Once everything is set up, just run the script to start downloading your playlists.
   
## Credits

Main Repository By **spotify-downloader** [Repository link](https://github.com/spotDL/spotify-downloader.git)

## LinkedIn [Sandeep Undrakonda](https://www.linkedin.com/in/sandeepundrakonda/)