#/usr/bin/python
import requests

def search_tracks(trackname,artist=""):
    query = "https://api.spotify.com/v1/search?q="
    if not artist :
        query=query+"\""+trackname+"\"&type=track"
    else:
        query=query+"\""+trackname+"\"+artist:\""+artist+"\"&type=track"
    r = requests.get(query)
    spotify_search_result_list = r.json()["tracks"]["items"]
    top_three_search_results = []
    top_three_search_results.append(choose_search_result(spotify_search_result_list[0]))
    if len(spotify_search_result_list)>1:
        top_three_search_results.append(choose_search_result(spotify_search_result_list[2]))
        if len(spotify_search_result_list)>2:
               top_three_search_results.append(choose_search_result(spotify_search_result_list[1]))
               
    return top_three_search_results

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

def choose_search_result(spotify_search_result):
    return  {"trackname": get_trackname(spotify_search_result), "artist": get_artist(spotify_search_result),"album": get_album(spotify_search_result),"spotify_id": get_spotify_id(spotify_search_result),"picture": get_album_picture(spotify_search_result)}

