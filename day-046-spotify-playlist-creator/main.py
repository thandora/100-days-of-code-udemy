"""Creates a playlist from billboard's top 100 on a user-input date.
"""


from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import os


def auth_spot() -> object:
    """Establish connection and authenticate to Spotify using spotipy library

    Returns:
        object: spotipy object
    """

    # Load env vars
    load_dotenv(".env")
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_SECRET")

    # Spotify requires this
    scope = "playlist-modify-private"
    redirect_uri = "http://example.com"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
    )

    return sp


def search_billboard(date: str) -> list:
    """Scrapes billboard for top 100 on the given <date>

    Args:
        date (str): date in YYYY-MM-DD

    Returns:
        list: list of disctionaries in the form:
        [ {<title>: <artist>},
         ...]
    """

    billboard_url = "https://www.billboard.com/charts/hot-100/"
    billboard_url = billboard_url + date

    html = requests.get(url=billboard_url).text

    titles = []
    artists = []
    soup = BeautifulSoup(html, features="html.parser")

    # This set alternates between song and artist. Add data accordingly.
    billboard = soup.select(
        ".lrv-u-width-100p .o-chart-results-list__item .a-no-trucate"
    )
    i = 0
    for song in billboard:
        if i == 0:
            titles.append(song.get_text().strip())
            i += 1
        else:
            artists.append(song.get_text().strip())
            i = 0

    song_list = []
    for i, title in enumerate(titles):
        song_list.append({"title": title, "artist": artists[i]})

    return song_list


def create_playlist(name: str, sp: object) -> str:
    """Creates blank playlist named <name>.

    Args:.
        name (str): Name of playlist
        sp (spotify Object): Spotify object currently authenticated.

    Returns:
        str: id of created playlist
    """

    user_id = sp.current_user().get("id")
    playlist_id = sp.user_playlist_create(user=user_id, name=name, public=False)

    return playlist_id.get("id")


def search_spotify(title: str, mode: str, year: int, artist: str) -> str:
    """Search track titled <title> on Spotify.

    Args:
        title (str): track title
        mode (str): "year" or "artist". Will filter the search result further
        using the specified mode.
        year (int): year if year mode is selected.
        artist (str): artist if artist mode is selected.

    Returns:
        str: URI (Unique Resource Identifier) of first match.
    """

    if mode.lower() == "year":
        search_query = f"track:{title} year:{year-2}-{year}"
    elif mode.lower() == "artist":
        search_query = f"track:{title} artist:{artist}"

    results = sp.search(q=search_query, type="track", limit=2)
    try:
        song_iden = results["tracks"]["items"][0]["uri"]

    # No search result
    except IndexError:
        song_iden = None

    return song_iden


def add_to_playlist(sp: object, id: str, songs_uri: list):
    """Add songs by their URIs in <songs_uri> into playlist specified by
    playlist id <id>.

    Args:
        sp (spotify Object): Spotify object currently authenticated.
        id (str): id of playlist on where to add tracks.
        songs_uri (list): list of track URIs
    """
    sp.playlist_add_items(playlist_id=id, items=songs_uri)


sp = auth_spot()
date = input("Which date would you want to travel to? (YYYY-MM-DD): ")
songs = search_billboard(date=date)
playlist_name = f"Billboards {date}"
playlist_id = create_playlist(name=playlist_name, sp=sp)

songs_uri = []
search_year = int(date[:4])
songs_total = len(songs)

# Populate <songs_uri> by songs found on billboard's top 100 in specified date.
for i, song in enumerate(songs):
    title = song.get("title")
    artist = song.get("artist")
    song_uri = search_spotify(title=title, artist=artist, year=search_year, mode="year")
    if song_uri is not None:
        songs_uri.append(song_uri)

        print(f"({(i+1)/songs_total}): Found: {title}")
    else:
        print(f"({(i+1)}/{songs_total}): Not Found: {title} by {artist}. Skipped.")
else:
    print(f"Found {len(songs_uri)}/{songs_total} songs")

add_to_playlist(sp=sp, id=playlist_id, songs_uri=songs_uri)
