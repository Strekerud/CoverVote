#/usr/bin/python
import requests

def gettrack(trackname,artist):
    query = "https://api.spotify.com/v1/search?q="
    if not artist :
        query=query+"\""+trackname+"\"&type=track"
    r = requests.get(query)
    spotify_search_result = r.json()["tracks"]["items"][0]
    return {"trackname": get_trackname(spotify_search_result), "artist": get_artist(spotify_search_result),"album": get_album(spotify_search_result),"id": get_spotify_id(spotify_search_result),"picture": get_album_picture(spotify_search_result)}

def get_trackname(spotify_search_result):
    return spotify_search_result["name"]

def get_artist(spotify_search_result):
    return spotify_search_result["artists"][0]["name"]

def get_album(spotify_search_result):
    return spotify_search_result["album"]["name"]

def get_spotify_id(spotify_search_result):
    return spotify_search_result["id"]

def get_album_picture(spotify_search_result):
    return spotify_search_result["album"]["images"][2]["url"]


